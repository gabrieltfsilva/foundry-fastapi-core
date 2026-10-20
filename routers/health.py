from fastapi import APIRouter, status
from core.config import settings
from models.health import HealthResponse

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health Check da Aplicação",
    description="Retorna o status operacional, versão e ambiente atual do microsserviço.",
)
async def health_check() -> HealthResponse:
    """Endpoint assíncrono para verificação de integridade do serviço."""
    return HealthResponse(
        status="healthy",
        project_name=settings.PROJECT_NAME,
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
    )
