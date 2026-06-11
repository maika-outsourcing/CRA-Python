from database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Collaborator(Base):
    __tablename__ = "collaborators"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)

    work_logs = relationship("WorkLog", back_populates="collaborator")


class WorkLog(Base):
    __tablename__ = "work_logs"

    id = Column(Integer, primary_key=True, index=True)
    collaborator_id = Column(Integer, ForeignKey("collaborators.id"))  # clé étrangère
    project = Column(String, index=True)
    task = Column(String)
    hours = Column(Float)
    date = Column(String)
    status = Column(String, default="En cours")
    description = Column(String, nullable=True)

    collaborator = relationship("Collaborator", back_populates="work_logs")
