from fastapi import FastAPI

from common.config.settings import ServiceSettings
from common.observability.logging import configure_logging
from common.schemas import WorkflowRequest

settings = ServiceSettings()
configure_logging(settings.service_name)
app = FastAPI(title=settings.service_name)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": settings.service_name}


@app.post("/execute")
def execute(request: WorkflowRequest) -> dict:
    return {
        "service": settings.service_name,
        "tenant_id": request.tenant_id,
        "document_count": len(request.document_urls),
        "summary": "placeholder for production agent logic",
    }
