from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.responsable import Responsable
from app.schemas.responsable import ResponsableCreate, ResponsableUpdate
from app.core.security import hash_password

async def get_responsable(db: AsyncSession, responsable_id: int):
    result = await db.execute(select(Responsable).where(Responsable.id == responsable_id))
    return result.scalar_one_or_none()

async def get_responsable_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(Responsable).where(Responsable.email == email))
    return result.scalar_one_or_none()

async def create_responsable(db: AsyncSession, responsable_in: ResponsableCreate):
    hashed_pw = hash_password(responsable_in.mot_de_passe)
    db_resp = Responsable(
        nom=responsable_in.nom,
        prenom=responsable_in.prenom,
        email=responsable_in.email,
        telephone=responsable_in.telephone,
        role=responsable_in.role,
        mot_de_passe=hashed_pw,
        actif=True,
    )
    db.add(db_resp)
    await db.commit()
    await db.refresh(db_resp)
    return db_resp

async def update_responsable(db: AsyncSession, responsable_id: int, responsable_in: ResponsableUpdate):
    resp = await get_responsable(db, responsable_id)
    if not resp:
        return None
    update_data = responsable_in.dict(exclude_unset=True)
    if "mot_de_passe" in update_data:
        update_data["mot_de_passe"] = hash_password(update_data["mot_de_passe"])
    for key, value in update_data.items():
        setattr(resp, key, value)
    db.add(resp)
    await db.commit()
    await db.refresh(resp)
    return resp

async def delete_responsable(db: AsyncSession, responsable_id: int):
    resp = await get_responsable(db, responsable_id)
    if not resp:
        return None
    await db.delete(resp)
    await db.commit()
    return resp

async def list_responsables(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Responsable).offset(skip).limit(limit))
    return result.scalars().all()
