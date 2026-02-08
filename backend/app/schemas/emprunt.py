from typing import Optional, Annotated
from pydantic import BaseModel, PositiveInt, constr
from datetime import date

MontantType = Annotated[float, PositiveInt()]  # si montant positif requis
TauxInteretType = Annotated[float, PositiveInt()]
DureeType = Annotated[int, PositiveInt()]

class EmpruntBase(BaseModel):
    montant: MontantType
    taux_interet: TauxInteretType
    date_emprunt: date
    duree_mois: DureeType
    membre_id: int  # lien vers membre (id)

class EmpruntCreate(EmpruntBase):
    pass

class EmpruntRead(EmpruntBase):
    id: int
    rembourse: bool

    class Config:
        orm_mode = True

class EmpruntUpdate(BaseModel):
    montant: Optional[MontantType] = None
    taux_interet: Optional[TauxInteretType] = None
    date_emprunt: Optional[date] = None
    duree_mois: Optional[DureeType] = None
    rembourse: Optional[bool] = None
