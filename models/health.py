from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Schema de resposta para verificação de saúde (Health Check) da API."""

    status: str = Field(..., examples=["healthy"], description="Status operacional do serviço")
    project_name: str = Field(..., examples=["Foundry FastAPI Core"], description="Nome do serviço")
    version: str = Field(..., examples=["0.1.0"], description="Versão atual da aplicação")
    environment: str = Field(..., examples=["development"], description="Ambiente de execução")
