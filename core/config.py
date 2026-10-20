from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações globais da aplicação gerenciadas via Pydantic Settings."""

    PROJECT_NAME: str = "Foundry FastAPI Core"
    DESCRIPTION: str = (
        "Microsserviço backend escalável pronto para integrações Cloud-Native e Azure AI Foundry."
    )
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Retorna uma instância em cache das configurações da aplicação."""
    return Settings()


settings = get_settings()
