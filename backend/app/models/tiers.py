from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Tiers(Base):
    __tablename__ = "tiers"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    telephone = Column(String, nullable=True)
    date_naissance = Column(Date, nullable=True)
    actif = Column(Boolean, default=True)
    mot_de_passe = Column(String, nullable=True)  # Peut être None si accès limité

    emprunts = relationship("Emprunt", back_populates="tiers")
