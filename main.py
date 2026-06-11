from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
import models
import database
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 👉 Ajout du middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Création des tables
models.Base.metadata.create_all(bind=database.engine)

# Obtenir la base de données
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schéma Pydantic pour création WorkLog
class WorkLogCreate(BaseModel):
    collaborator_id: int
    project: str
    task: str
    hours: float
    date: str
    status: str = "En cours"
    description: Optional[str] = None

# Schéma Pydantic pour lecture WorkLog
class WorkLogRead(BaseModel):
    id: int
    collaborator_id: int
    collaborator_name: Optional[str] = None
    project: str
    task: str
    hours: float
    date: str
    status: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

# Endpoint POST : ajouter un WorkLog
@app.post("/work_logs", response_model=WorkLogRead)
def create_work_log(worklog: WorkLogCreate, db: Session = Depends(get_db)):
    new_log = models.WorkLog(**worklog.dict())
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return WorkLogRead(
        id=new_log.id,
        collaborator_id=new_log.collaborator_id,
        collaborator_name=new_log.collaborator.name if new_log.collaborator else None,
        project=new_log.project,
        task=new_log.task,
        hours=new_log.hours,
        date=new_log.date,
        status=new_log.status,
        description=new_log.description,
    )

# Endpoint GET : lister WorkLogs
@app.get("/work_logs", response_model=list[WorkLogRead])
def read_work_logs(db: Session = Depends(get_db)):
    logs = (
        db.execute(
            select(models.WorkLog).options(joinedload(models.WorkLog.collaborator))
        )
        .scalars()
        .all()
    )
    return [
        WorkLogRead(
            id=log.id,
            collaborator_id=log.collaborator_id,
            collaborator_name=log.collaborator.name if log.collaborator else None,
            project=log.project,
            task=log.task,
            hours=log.hours,
            date=log.date,
            status=log.status,
            description=log.description,
        )
        for log in logs
    ]

# Schéma pour mise à jour WorkLog
class WorkLogUpdate(BaseModel):
    collaborator_id: Optional[int] = None
    project: Optional[str] = None
    task: Optional[str] = None
    hours: Optional[float] = None
    date: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None

# Endpoint PUT : mise à jour WorkLog
@app.put("/work_logs/{log_id}", response_model=WorkLogRead)
def update_work_log(log_id: int, worklog: WorkLogUpdate, db: Session = Depends(get_db)):
    log = db.get(models.WorkLog, log_id)
    if not log:
        return {"erreur": "Entrée non trouvée"}
    for var, value in worklog.dict(exclude_unset=True).items():
        setattr(log, var, value)
    db.commit()
    db.refresh(log)
    return WorkLogRead(
        id=log.id,
        collaborator_id=log.collaborator_id,
        collaborator_name=log.collaborator.name if log.collaborator else None,
        project=log.project,
        task=log.task,
        hours=log.hours,
        date=log.date,
        status=log.status,
        description=log.description,
    )

# Schémas Pydantic pour Collaborator
class CollaboratorBase(BaseModel):
    name: str
    email: Optional[str] = None

class CollaboratorCreate(CollaboratorBase):
    pass

class CollaboratorRead(CollaboratorBase):
    id: int
    class Config:
        orm_mode = True

# Endpoint POST : ajouter un collaborateur
@app.post("/collaborators", response_model=CollaboratorRead)
def create_collaborator(collaborator: CollaboratorCreate, db: Session = Depends(get_db)):
    new_collaborator = models.Collaborator(**collaborator.dict())
    db.add(new_collaborator)
    db.commit()
    db.refresh(new_collaborator)
    return new_collaborator

# Endpoint GET : lister les collaborateurs
@app.get("/collaborators", response_model=list[CollaboratorRead])
def read_collaborators(db: Session = Depends(get_db)):
    return db.execute(select(models.Collaborator)).scalars().all()
