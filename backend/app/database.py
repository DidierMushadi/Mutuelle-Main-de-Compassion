from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator
from app.core.config import settings  # Ton fichier de config avec DB_USER, DB_PASSWORD, etc.

# Base SQLAlchemy pour les modèles
Base = declarative_base()

# Construction de l'URL de connexion async à PostgreSQL
DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{settings.DB_USER}:{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)

# Création de l'engine async
engine = create_async_engine(
    DATABASE_URL,
    echo=False,  # True pour debug SQL
    future=True,  # utilise la nouvelle API SQLAlchemy 2.0
    pool_pre_ping=True,
)

# Création du sessionmaker async
async_session_maker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
    autoflush=False,
)

# Dépendance FastAPI pour obtenir la session de base de données
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
