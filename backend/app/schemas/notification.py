from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    titre: str
    message: str
    date_envoi: Optional[datetime] = None
    destinataire_id: Optional[int] = None  # id du membre ou responsable

class NotificationCreate(NotificationBase):
    pass

class NotificationRead(NotificationBase):
    id: int

    class Config:
        from_attributes = True  # Remplace orm_mode pour Pydantic v2

class NotificationUpdate(BaseModel):
    titre: Optional[str] = None
    message: Optional[str] = None
    date_envoi: Optional[datetime] = None
    destinataire_id: Optional[int] = None
