from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.member import Member
from app.schemas.member import MemberCreate, MemberUpdate
from app.core.security import hash_password

async def get_member(db: AsyncSession, member_id: int):
    result = await db.execute(select(Member).where(Member.id == member_id))
    return result.scalar_one_or_none()

async def get_member_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(Member).where(Member.email == email))
    return result.scalar_one_or_none()

async def create_member(db: AsyncSession, member_in: MemberCreate):
    hashed_pw = hash_password(member_in.mot_de_passe)
    db_member = Member(
        nom=member_in.nom,
        prenom=member_in.prenom,
        email=member_in.email,
        telephone=member_in.telephone,
        date_naissance=member_in.date_naissance,
        mot_de_passe=hashed_pw,
        actif=True,
    )
    db.add(db_member)
    await db.commit()
    await db.refresh(db_member)
    return db_member

async def update_member(db: AsyncSession, member_id: int, member_in: MemberUpdate):
    member = await get_member(db, member_id)
    if not member:
        return None
    update_data = member_in.dict(exclude_unset=True)
    if "mot_de_passe" in update_data:
        update_data["mot_de_passe"] = hash_password(update_data["mot_de_passe"])
    for key, value in update_data.items():
        setattr(member, key, value)
    db.add(member)
    await db.commit()
    await db.refresh(member)
    return member

async def delete_member(db: AsyncSession, member_id: int):
    member = await get_member(db, member_id)
    if not member:
        return None
    await db.delete(member)
    await db.commit()
    return member

async def list_members(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Member).offset(skip).limit(limit))
    return result.scalars().all()
