from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import database
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 👉 Ajout du middleware CORS juste après la création de l'app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ton frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Creation des tables
models.Base.metadata.create_all(bind=database.engine)

#Obtenir la base de données
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Schema Pydantic pour la validation des données reçues
class WorkLogCreate(BaseModel):
    project: str
    task: str
    hours: float
    date: str
    status: str = "En cours"       # valeur par défaut
    description: str | None = None # optionnel

# Endpoint POST : ajouter une entrée
@app.post("/work_logs")
def create_work_log(worklog: WorkLogCreate, db: Session = Depends(get_db)):
    new_log = models.WorkLog(
        project=worklog.project,
        task=worklog.task,
        hours=worklog.hours,
        date=worklog.date,
        status=worklog.status,
        description=worklog.description
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

# Endpoint GET : lister toutes les entrées
@app.get("/work_logs")
def read_work_logs(db: Session = Depends(get_db)):
    return db.query(models.WorkLog).all()

#Schéma pour mettre à jour partiellement une entrée
class WorkLogUpdate(BaseModel):
    project: Optional[str] = None
    task: Optional[str] = None
    hours: Optional[float] = None
    date: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None

# Endpoint PUT : mettre à jour une entrée
@app.put("/work_logs/{log_id}")
def update_work_log(log_id: int, worklog: WorkLogUpdate, db: Session = Depends(get_db)):
    log = db.query(models.WorkLog).filter(models.WorkLog.id == log_id).first()
    if not log:
        return {"erreur": "Entrée non trouvée"}
    
    #Mettre à jour uniquement les champs fournis
    for var, value in worklog.dict(exclude_unset=True).items():
        if value is not None:
            setattr(log, var, value)
    
    db.commit()
    db.refresh(log)
    return log
