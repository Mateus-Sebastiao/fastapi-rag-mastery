import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application core configurations using Pydantic Settings.
    Loads variables from system environment or .env file.
    """
    APP_NAME: str = "FastAPI RAG Mastery"
    ENVIRONMENT: str = "development"
    
    # AI Infrastructure Gateway configurations
    LITELLM_PROXY_URL: str = "http://localhost:4000"
    OLLAMA_API_BASE: str = "http://localhost:11434"
    
    # Vector Database storage parameters
    CHROMA_PERSIST_DIR: str = "./chroma_db"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
