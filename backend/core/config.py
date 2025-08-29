from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = True

    DATABASE_URL: str = "sqlite:///./database.db"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    OPENAI_API_KEY: str = "your_openai_api_key_here"
    GEMINI_API_KEY: str = "AIzaSyDe2N5djkn43nuszWIcraqRRBAWJxo9rcU"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()