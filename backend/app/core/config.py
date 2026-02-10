from pydantic_settings import BaseSettings
from pydantic import EmailStr
from typing import Optional

class Settings(BaseSettings):
    # ======================
    # Base de données
    # ======================
    DB_HOST: str = "localhost"         # valeur par défaut pour dev
    DB_PORT: int = 5432
    DB_NAME: str = "mutuelle_dev"
    DB_USER: str = "dev_user"
    DB_PASSWORD: str = "dev_password"

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
        env_file = ".env"       # charger depuis .env à la racine du projet
        extra = "ignore"        # ignorer les variables inconnues

# Instance globale
settings = Settings()
