from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.tiers import Tiers
from app.schemas.tiers import TiersCreate, TiersUpdate

async def get_tiers(db: AsyncSession, tiers_id: int):
    result = await db.execute(select(Tiers).where(Tiers.id == tiers_id))
    return result.scalar_one_or_none()

async def create_tiers(db: AsyncSession, tiers_in: TiersCreate):
    db_tiers = Tiers(
        nom=tiers_in.nom,
        prenom=tiers_in.prenom,
        email=tiers_in.email,
        telephone=tiers_in.telephone,
        actif=True,
    )
    db.add(db_tiers)
    await db.commit()
    await db.refresh(db_tiers)
    return db_tiers

async def update_tiers(db: AsyncSession, tiers_id: int, tiers_in: TiersUpdate):
    tiers = await get_tiers(db, tiers_id)
    if not tiers:
        return None
    update_data = tiers_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(tiers, key, value)
    db.add(tiers)
    await db.commit()
    await db.refresh(tiers)
    return tiers

async def delete_tiers(db: AsyncSession, tiers_id: int):
    tiers = await get_tiers(db, tiers_id)
    if not tiers:
        return None
    await db.delete(tiers)
    await db.commit()
    return tiers

async def list_tiers(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Tiers).offset(skip).limit(limit))
    return result.scalars().all()
