from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Centralized application configuration.
    Values are loaded from environment variables when present.
    """

    app_name: str = "production-rag-agentic-system"
    environment: str = "development"
    log_level: str = "INFO"

    class Config:
        env_prefix = "APP_"


settings = Settings()

