from fastapi.testclient import TestClient
from core.config import settings
from main import app

client = TestClient(app)


def test_health_check_returns_200_and_expected_payload():
    """Deve retornar HTTP 200 e o payload de saúde esperado conforme HealthResponse."""
    response = client.get(f"{settings.API_V1_STR}/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["project_name"] == settings.PROJECT_NAME
    assert data["version"] == settings.VERSION
    assert data["environment"] == settings.ENVIRONMENT


def test_root_redirects_to_docs():
    """Deve redirecionar a rota raiz (/) para a documentação Swagger (/docs)."""
    response = client.get("/", follow_redirects=False)

    assert response.status_code in (307, 302)
    assert response.headers["location"] == "/docs"
