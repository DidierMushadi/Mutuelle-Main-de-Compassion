from sqlalchemy import Column, Integer, Float, Date, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Paiement(Base):
    __tablename__ = "paiements"

    id = Column(Integer, primary_key=True, index=True)
    montant = Column(Float, nullable=False)
    date_paiement = Column(Date, nullable=False)
    type_paiement = Column(String, nullable=False)  # souscription, remboursement
    penalite_appliquee = Column(Boolean, default=False)
    penalite_montant = Column(Float, default=0.0)

    member_id = Column(Integer, ForeignKey("members.id"))
    member = relationship("Member", back_populates="paiements")
