from fastapi.testclient import TestClient
from core.config import settings
from main import app

client = TestClient(app)


def test_health_check_returns_200_and_expected_payload():
    """Should return HTTP 200 and the expected health payload matching HealthResponse."""
    response = client.get(f"{settings.API_V1_STR}/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["project_name"] == settings.PROJECT_NAME
    assert data["version"] == settings.VERSION
    assert data["environment"] == settings.ENVIRONMENT


def test_root_redirects_to_docs():
    """Should redirect the root route (/) to the Swagger documentation (/docs)."""
    response = client.get("/", follow_redirects=False)

    assert response.status_code in (307, 302)
    assert response.headers["location"] == "/docs"
