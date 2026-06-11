from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Connexion à la base SQLite (fichier local)
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# Engine : le moteur qui parle à la base
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal : fabrique de sessions pour interagir avec la base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base déclarative (style SQLAlchemy 2.0)
class Base(DeclarativeBase):
    pass

