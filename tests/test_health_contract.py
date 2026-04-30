from fastapi.testclient import TestClient

from services.extract_agent_service.app.main import app


def test_health() -> None:
    client = TestClient(app)
    resp = client.get('/health')
    assert resp.status_code == 200
