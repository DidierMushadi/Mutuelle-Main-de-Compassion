from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.paiement import Paiement
from app.schemas.paiement import PaiementCreate, PaiementUpdate

async def get_paiement(db: AsyncSession, paiement_id: int):
    result = await db.execute(select(Paiement).where(Paiement.id == paiement_id))
    return result.scalar_one_or_none()

async def create_paiement(db: AsyncSession, paiement_in: PaiementCreate):
    db_paiement = Paiement(
        montant=paiement_in.montant,
        date=paiement_in.date,
        type_paiement=paiement_in.type_paiement,
        member_id=paiement_in.member_id,
    )
    db.add(db_paiement)
    await db.commit()
    await db.refresh(db_paiement)
    return db_paiement

async def update_paiement(db: AsyncSession, paiement_id: int, paiement_in: PaiementUpdate):
    paiement = await get_paiement(db, paiement_id)
    if not paiement:
        return None
    update_data = paiement_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(paiement, key, value)
    db.add(paiement)
    await db.commit()
    await db.refresh(paiement)
    return paiement

async def delete_paiement(db: AsyncSession, paiement_id: int):
    paiement = await get_paiement(db, paiement_id)
    if not paiement:
        return None
    await db.delete(paiement)
    await db.commit()
    return paiement

async def list_paiements(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Paiement).offset(skip).limit(limit))
    return result.scalars().all()
