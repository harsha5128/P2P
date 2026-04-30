import asyncio
import uuid

import httpx
from fastapi import FastAPI, HTTPException

from common.config.settings import ServiceSettings
from common.observability.logging import configure_logging
from common.schemas import AgentResult, WorkflowRequest, WorkflowResponse

settings = ServiceSettings()
configure_logging(settings.service_name)
app = FastAPI(title="Orchestrator Service")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": settings.service_name}


@app.post("/workflows/run", response_model=WorkflowResponse)
async def run_workflow(request: WorkflowRequest) -> WorkflowResponse:
    workflow_id = str(uuid.uuid4())
    stages = [
        ("extract", settings.extract_url),
        ("validate", settings.validation_url),
        ("approve_pay", settings.approval_url),
        ("sla", settings.sla_url),
        ("query_writer", settings.query_writer_url),
    ]

    results: list[AgentResult] = []
    async with httpx.AsyncClient(timeout=30) as client:
        for stage, base_url in stages:
            try:
                resp = await client.post(f"{base_url}/execute", json=request.model_dump())
                resp.raise_for_status()
                payload = resp.json()
                results.append(AgentResult(stage=stage, status="success", details=payload))
            except Exception as exc:  # noqa: BLE001
                results.append(AgentResult(stage=stage, status="failed", details={"error": str(exc)}))
                raise HTTPException(status_code=502, detail=f"{stage} failed") from exc
            await asyncio.sleep(0.01)

    return WorkflowResponse(workflow_id=workflow_id, status="completed", results=results)
