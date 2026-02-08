from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import delete
from typing import List, Optional
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate, NotificationUpdate

# Créer une nouvelle notification
async def create_notification(
    db: AsyncSession, notification_in: NotificationCreate
) -> Notification:
    new_notification = Notification(**notification_in.dict())
    db.add(new_notification)
    await db.commit()
    await db.refresh(new_notification)
    return new_notification

# Obtenir une notification par son ID
async def get_notification(
    db: AsyncSession, notification_id: int
) -> Optional[Notification]:
    result = await db.execute(select(Notification).where(Notification.id == notification_id))
    return result.scalars().first()

# Lister toutes les notifications avec pagination
async def list_notifications(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> List[Notification]:
    result = await db.execute(select(Notification).offset(skip).limit(limit))
    return result.scalars().all()

# Mettre à jour une notification existante
async def update_notification(
    db: AsyncSession, notification_id: int, notification_in: NotificationUpdate
) -> Optional[Notification]:
    notification = await get_notification(db, notification_id)
    if not notification:
        return None
    for key, value in notification_in.dict(exclude_unset=True).items():
        setattr(notification, key, value)
    db.add(notification)
    await db.commit()
    await db.refresh(notification)
    return notification

# Supprimer une notification
async def delete_notification(
    db: AsyncSession, notification_id: int
) -> bool:
    notification = await get_notification(db, notification_id)
    if not notification:
        return False
    await db.delete(notification)
    await db.commit()
    return True
