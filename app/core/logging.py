# app/core/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "LLM RAG Service"
    environment: str = "dev"

    # API
    host: str = "0.0.0.0"
    port: int = 8000

    # Vector DB (future)
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333

    class Config:
        env_file = ".env"


settings = Settings()
