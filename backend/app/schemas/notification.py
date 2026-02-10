from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class NotificationBase(BaseModel):
    titre: str
    message: str
    date_envoi: Optional[datetime] = None
    destinataire_id: Optional[int] = None  # id du membre ou responsable


class NotificationCreate(NotificationBase):
    pass


class NotificationRead(NotificationBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class NotificationUpdate(BaseModel):
    titre: Optional[str] = None
    message: Optional[str] = None
    date_envoi: Optional[datetime] = None
    destinataire_id: Optional[int] = None
