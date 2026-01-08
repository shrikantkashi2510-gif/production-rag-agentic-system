from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.logging import configure_logging


def create_app() -> FastAPI:
    """
    Application factory.
    Keeps app creation explicit and testable.
    """
    configure_logging()

    app = FastAPI(
        title="Production RAG Agentic System",
        description="API-first LLM and agentic AI service",
        version="0.1.0",
    )

    app.include_router(api_router, prefix="/api")

    return app



app = create_app()

