from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Responsable(Base):
    __tablename__ = "responsables"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telephone = Column(String, nullable=True)
    role = Column(String, nullable=False)  # Ex: PDG, Comptable, Caissier
    mot_de_passe = Column(String, nullable=False)
    actif = Column(Boolean, default=True)

    # Relations éventuelles
