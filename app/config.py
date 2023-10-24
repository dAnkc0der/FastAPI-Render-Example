from pydantic_settings import BaseSettings
from app import database

class Settings(BaseSettings):
    # database_hostname: str
    # database_port: str
    # database_password: str
    # database_name: str
    # database_username: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
