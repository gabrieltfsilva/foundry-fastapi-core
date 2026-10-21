from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Response schema for the API health check endpoint."""

    status: str = Field(..., examples=["healthy"], description="Operational status of the service")
    project_name: str = Field(..., examples=["Foundry FastAPI Core"], description="Service name")
    version: str = Field(..., examples=["0.1.0"], description="Current application version")
    environment: str = Field(..., examples=["development"], description="Execution environment")
