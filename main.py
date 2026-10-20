from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from core.config import settings
from routers import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gerencia o ciclo de vida da aplicação (Startup e Shutdown).
    Futuramente inicializará e fechará clientes persistentes do Azure AI Foundry.
    """
    # Startup: inicializar conexões/clientes (ex: AIProjectClient, DefaultAzureCredential)
    yield
    # Shutdown: liberar recursos e conexões HTTP graciosamente


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Registro de Routers sob o prefixo /api/v1
app.include_router(health.router, prefix=settings.API_V1_STR)


@app.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    """Redireciona a rota raiz para a documentação interativa (Swagger UI)."""
    return RedirectResponse(url="/docs")
