from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.emprunt import Emprunt
from app.schemas.emprunt import EmpruntCreate, EmpruntUpdate

async def get_emprunt(db: AsyncSession, emprunt_id: int):
    result = await db.execute(select(Emprunt).where(Emprunt.id == emprunt_id))
    return result.scalar_one_or_none()

async def create_emprunt(db: AsyncSession, emprunt_in: EmpruntCreate):
    db_emprunt = Emprunt(
        montant=emprunt_in.montant,
        taux_interet=emprunt_in.taux_interet,
        date_debut=emprunt_in.date_debut,
        date_fin=emprunt_in.date_fin,
        member_id=emprunt_in.member_id,
        tiers_id=emprunt_in.tiers_id,
    )
    db.add(db_emprunt)
    await db.commit()
    await db.refresh(db_emprunt)
    return db_emprunt

async def update_emprunt(db: AsyncSession, emprunt_id: int, emprunt_in: EmpruntUpdate):
    emprunt = await get_emprunt(db, emprunt_id)
    if not emprunt:
        return None
    update_data = emprunt_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(emprunt, key, value)
    db.add(emprunt)
    await db.commit()
    await db.refresh(emprunt)
    return emprunt

async def delete_emprunt(db: AsyncSession, emprunt_id: int):
    emprunt = await get_emprunt(db, emprunt_id)
    if not emprunt:
        return None
    await db.delete(emprunt)
    await db.commit()
    return emprunt

async def list_emprunts(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Emprunt).offset(skip).limit(limit))
    return result.scalars().all()
