# Agentic AI Procurement Automation System (P2P)

Enterprise-grade microservices starter for procure-to-pay automation with an agentic architecture.

## Architecture
- **orchestrator-service**: CrewAI/LangGraph-compatible control plane for stage sequencing, retries, and dependency handling.
- **extract-agent-service**: OCR/LLM extraction agent for PO/GRN/invoice payloads.
- **validation-agent-service**: 2-way/3-way matching, anomaly detection, and policy validation.
- **approval-payment-service**: auto-approval and payment decisioning.
- **sla-agent-service**: SLA timers, escalation, and breach alerts.
- **query-writer-service**: stakeholder query/response generation and audit narratives.
- **MongoDB**: audit and workflow persistence.
- **API Gateway (Nginx)**: ingress routing.

## Repo Layout
- `services/`: independently deployable FastAPI services.
- `common/`: shared schemas, config, logging.
- `infra/`: gateway config, database bootstrap, infra placeholders.
- `docs/`: architecture and production runbooks.
- `tests/`: baseline tests.

## Quickstart
```bash
pip install -e .[dev]
docker compose up --build
```

Run workflow (example):
```bash
curl -X POST http://localhost:8080/orchestrator/workflows/run \
  -H "content-type: application/json" \
  -d '{"tenant_id":"acme","document_urls":["s3://bucket/invoice-1.pdf"]}'
```

## Production Roadmap
1. Replace placeholder `/execute` handlers with CrewAI + LangGraph graphs per service.
2. Add message bus (SQS/Kafka) for async orchestration and DLQ.
3. Add policy engine (OPA) and external ERP adapters (SAP/Oracle/NetSuite).
4. Enable LangFuse tracing + OpenTelemetry.
5. Harden auth (OIDC, mTLS), secrets (AWS Secrets Manager), and compliance controls.
