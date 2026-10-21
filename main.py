from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from core.config import settings
from routers import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage application lifecycle (Startup and Shutdown).
    Will initialize and close persistent Azure AI Foundry clients in future steps.
    """
    # Startup: initialize connections/clients (e.g., AIProjectClient, DefaultAzureCredential)
    yield
    # Shutdown: gracefully release resources and HTTP connections


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Register routers under the /api/v1 prefix
app.include_router(health.router, prefix=settings.API_V1_STR)


@app.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    """Redirect the root route to the interactive API documentation (Swagger UI)."""
    return RedirectResponse(url="/docs")
