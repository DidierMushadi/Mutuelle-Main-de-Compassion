from sqlalchemy import Column, Integer, Float, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base

class Emprunt(Base):
    __tablename__ = "emprunts"

    id = Column(Integer, primary_key=True, index=True)
    montant = Column(Float, nullable=False)
    taux_interet = Column(Float, nullable=False)  # en %, ex: 5.0
    date_debut = Column(Date, nullable=False)
    date_echeance = Column(Date, nullable=False)
    statut = Column(String, default="en_cours")  # en_cours, payé, en_retard, etc.

    # Liens vers les emprunteurs : membre ou tiers
    member_id = Column(Integer, ForeignKey("members.id"), nullable=True)
    tiers_id = Column(Integer, ForeignKey("tiers.id"), nullable=True)

    member = relationship("Member", back_populates="emprunts")
    tiers = relationship("Tiers", back_populates="emprunts")
