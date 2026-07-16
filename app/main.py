from fastapi import FastAPI
from app.core.config import settings
from app.modules.beginner.router import router as beginner_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Production-grade local architecture roadmap from basic RAG systems to Agents."
)

# Standard Healthcheck endpoint
@app.get("/health", tags=["Infrastructure"])
async def health_check():
    return {"status": "healthy", "environment": settings.ENVIRONMENT}

# Routing registration modules mapping
app.include_router(beginner_router)
