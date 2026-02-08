from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.notification import NotificationCreate, NotificationRead, NotificationUpdate
from app.crud.notification import create_notification, get_notification, list_notifications, update_notification, delete_notification
from app.core.security import get_current_active_user, verify_role
from app.database import get_db

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.post("/", response_model=NotificationRead)
async def create_new_notification(
    notification_in: NotificationCreate,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    # Seul le PDG peut créer
    if not verify_role(current_user, ["pdg"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission refusée")
    return await create_notification(db, notification_in)

@router.get("/{notification_id}", response_model=NotificationRead)
async def read_notification(
    notification_id: int,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    notification = await get_notification(db, notification_id)
    if not notification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification non trouvée")
    # PDG ou responsable peuvent accéder
    if not verify_role(current_user, ["pdg", "responsable"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission refusée")
    return notification

@router.get("/", response_model=List[NotificationRead])
async def read_notifications(
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    # PDG et responsables peuvent lister
    if not verify_role(current_user, ["pdg", "responsable"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission refusée")
    return await list_notifications(db, skip=skip, limit=limit)

@router.put("/{notification_id}", response_model=NotificationRead)
async def update_existing_notification(
    notification_id: int,
    notification_in: NotificationUpdate,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    if not verify_role(current_user, ["pdg"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission refusée")
    notification = await update_notification(db, notification_id, notification_in)
    if not notification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification non trouvée")
    return notification

@router.delete("/{notification_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_notification(
    notification_id: int,
    current_user=Depends(get_current_active_user),
    db: AsyncSession = Depends(get_db),
):
    if not verify_role(current_user, ["pdg"]):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission refusée")
    await delete_notification(db, notification_id)
