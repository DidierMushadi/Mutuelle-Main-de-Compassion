from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telephone = Column(String, nullable=True)
    date_naissance = Column(Date, nullable=True)
    actif = Column(Boolean, default=True)
    mot_de_passe = Column(String, nullable=False)

    # Relations
    paiements = relationship("Paiement", back_populates="member")
    emprunts = relationship("Emprunt", back_populates="member")
