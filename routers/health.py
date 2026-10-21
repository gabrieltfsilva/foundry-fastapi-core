from fastapi import APIRouter, status
from core.config import settings
from models.health import HealthResponse

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Application Health Check",
    description="Returns the operational status, version, and current environment of the microservice.",
)
async def health_check() -> HealthResponse:
    """Asynchronous endpoint for service health verification."""
    return HealthResponse(
        status="healthy",
        project_name=settings.PROJECT_NAME,
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
    )
