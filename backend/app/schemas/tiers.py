from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, constr
from datetime import date

NomType = Annotated[str, constr(min_length=1)]
PrenomType = Annotated[str, constr(min_length=1)]

class TiersBase(BaseModel):
    nom: NomType
    prenom: PrenomType
    email: Optional[EmailStr] = None
    telephone: Optional[str] = None
    date_naissance: Optional[date] = None

class TiersCreate(TiersBase):
    mot_de_passe: Annotated[str, constr(min_length=6)]

class TiersRead(TiersBase):
    id: int
    actif: bool

    class Config:
        orm_mode = True

class TiersUpdate(BaseModel):
    nom: Optional[NomType] = None
    prenom: Optional[PrenomType] = None
    email: Optional[EmailStr] = None
    telephone: Optional[str] = None
    date_naissance: Optional[date] = None
    actif: Optional[bool] = None
