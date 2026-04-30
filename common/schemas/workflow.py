from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field


class WorkflowRequest(BaseModel):
    tenant_id: str
    document_urls: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class AgentResult(BaseModel):
    stage: str
    status: str
    details: dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class WorkflowResponse(BaseModel):
    workflow_id: str
    status: str
    results: list[AgentResult]
