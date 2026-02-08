from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.member import MemberCreate, MemberRead, MemberUpdate
from app.crud.member import (
    create_member,
    get_member,
    list_members,
    update_member,
    delete_member,
)
from app.core.security import get_current_active_user, verify_role
from app.database import get_db

router = APIRouter(
    prefix="/members",
    tags=["members"]
)

@router.post("/", response_model=MemberRead)
async def create_new_member(
    member_in: MemberCreate,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    if not verify_role(current_user, ["pdg"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission refusée"
        )
    return await create_member(db, member_in)


@router.get("/{member_id}", response_model=MemberRead)
async def read_member(
    member_id: int,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    member = await get_member(db, member_id)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Membre non trouvé"
        )

    if current_user.id != member_id and not verify_role(current_user, ["pdg"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission refusée"
        )
    return member


@router.get("/", response_model=List[MemberRead])
async def read_members(
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    if not verify_role(current_user, ["pdg"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission refusée"
        )
    return await list_members(db, skip=skip, limit=limit)


@router.put("/{member_id}", response_model=MemberRead)
async def update_existing_member(
    member_id: int,
    member_in: MemberUpdate,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    if current_user.id != member_id and not verify_role(current_user, ["pdg"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission refusée"
        )

    member = await update_member(db, member_id, member_in)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Membre non trouvé"
        )
    return member


@router.delete("/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_member(
    member_id: int,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    if not verify_role(current_user, ["pdg"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission refusée"
        )
    await delete_member(db, member_id)
