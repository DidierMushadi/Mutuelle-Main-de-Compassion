from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.responsable import ResponsableCreate, ResponsableRead, ResponsableUpdate
from app.crud.responsable import create_responsable, get_responsable, list_responsables, update_responsable, delete_responsable
from app.core.security import get_current_active_user, verify_role
from app.database import get_db

router = APIRouter(prefix="/responsables", tags=["responsables"])

@router.post("/", response_model=ResponsableRead)
async def create_new_responsable(
    responsable_in: ResponsableCreate,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    if not verify_role(current_user, ["pdg"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission refusée")
    return await create_responsable(db, responsable_in)

@router.get("/{responsable_id}", response_model=ResponsableRead)
async def read_responsable(
    responsable_id: int,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    responsable = await get_responsable(db, responsable_id)
    if not responsable:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Responsable non trouvé")
    # Autoriser que PDG ou le responsable lui-même
    if current_user.id != responsable_id and not verify_role(current_user, ["pdg"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission refusée")
    return responsable

@router.get("/", response_model=List[ResponsableRead])
async def read_responsables(
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    if not verify_role(current_user, ["pdg"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission refusée")
    return await list_responsables(db, skip=skip, limit=limit)

@router.put("/{responsable_id}", response_model=ResponsableRead)
async def update_existing_responsable(
    responsable_id: int,
    responsable_in: ResponsableUpdate,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    if not verify_role(current_user, ["pdg"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission refusée")
    responsable = await update_responsable(db, responsable_id, responsable_in)
    if not responsable:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Responsable non trouvé")
    return responsable

@router.delete("/{responsable_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_responsable(
    responsable_id: int,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    if not verify_role(current_user, ["pdg"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission refusée")
    await delete_responsable(db, responsable_id)
