from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, constr
from datetime import date

NomType = Annotated[str, constr(min_length=1)]
PrenomType = Annotated[str, constr(min_length=1)]
PasswordType = Annotated[str, constr(min_length=6)]

class MemberBase(BaseModel):
    nom: NomType
    prenom: PrenomType
    email: EmailStr
    telephone: Optional[str]
    date_naissance: Optional[date]

class MemberCreate(MemberBase):
    mot_de_passe: PasswordType

class MemberRead(MemberBase):
    id: int
    actif: bool

    class Config:
        from_attributes = True  # Mis à jour pour Pydantic v2

class MemberUpdate(BaseModel):
    nom: Optional[NomType]
    prenom: Optional[PrenomType]
    email: Optional[EmailStr]
    telephone: Optional[str]
    date_naissance: Optional[date]
    actif: Optional[bool]
