from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.middleware import observability_middleware   # ✅ add this import
from app.routers.analyze import router as analyze_router
import logging

setup_logging(settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.APP_NAME)

# ✅ ADD THIS LINE HERE (immediately after app creation)
app.middleware("http")(observability_middleware)

app.include_router(analyze_router)

@app.get("/health")
def health():
    logger.info("Health check called")
    return {
        "status": "ok",
        "env": settings.APP_ENV
    }
