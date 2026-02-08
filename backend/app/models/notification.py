from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    date_envoi = Column(DateTime, default=datetime.utcnow)
    lu = Column(Boolean, default=False)

    responsable_id = Column(Integer, ForeignKey("responsables.id"), nullable=True)
    membre_id = Column(Integer, ForeignKey("members.id"), nullable=True)

    # Relations
    responsable = relationship("Responsable")
    membre = relationship("Member")
