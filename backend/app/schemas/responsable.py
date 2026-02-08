from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, constr

NomType = Annotated[str, constr(min_length=1)]
PrenomType = Annotated[str, constr(min_length=1)]
PasswordType = Annotated[str, constr(min_length=6)]

class ResponsableBase(BaseModel):
    nom: NomType
    prenom: PrenomType
    email: EmailStr
    telephone: Optional[str]

class ResponsableCreate(ResponsableBase):
    mot_de_passe: PasswordType

class ResponsableRead(ResponsableBase):
    id: int
    actif: bool

    class Config:
        from_attributes = True  # Mis à jour

class ResponsableUpdate(BaseModel):
    nom: Optional[NomType]
    prenom: Optional[PrenomType]
    email: Optional[EmailStr]
    telephone: Optional[str]
    actif: Optional[bool]
