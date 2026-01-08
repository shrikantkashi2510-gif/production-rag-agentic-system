from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["system"])
def health_check() -> dict:
    """
    Health check endpoint used by load balancers and monitoring.
    """
    return {
        "status": "ok",
        "service": "production-rag-agentic-system",
    }

