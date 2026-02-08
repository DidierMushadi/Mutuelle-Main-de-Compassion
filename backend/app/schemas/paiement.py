from typing import Optional
from pydantic import BaseModel
from datetime import date

class PaiementBase(BaseModel):
    montant: float
    date_paiement: Optional[date] = None
    membre_id: int

class PaiementCreate(PaiementBase):
    pass

class PaiementRead(PaiementBase):
    id: int

    class Config:
        from_attributes = True  # Mis à jour

class PaiementUpdate(BaseModel):
    montant: Optional[float] = None
    date_paiement: Optional[date] = None
    membre_id: Optional[int] = None
