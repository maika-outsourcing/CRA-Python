from database import Base
from sqlalchemy import Column, Integer, String, Float

class WorkLog(Base):
    __tablename__ = "work_logs"

    id = Column(Integer, primary_key=True, index=True)
    project = Column(String, index=True)
    task = Column(String)
    hours = Column(Float)
    date = Column(String) 
    status = Column(String, default="En cours")  # nouveau champ
    description = Column(String, nullable=True)  # nouveau champ
