from pydantic_settings import BaseSettings
from pydantic import EmailStr
from typing import Optional


class Settings(BaseSettings):
    # ======================
    # Base de données
    # ======================
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # ======================
    # Sécurité
    # ======================
    SECRET_KEY: str = "change_me_in_production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # ======================
    # Application
    # ======================
    APP_NAME: str = "Mutuelle Main de Compassion UMOJA"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
