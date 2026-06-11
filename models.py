from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Collaborator(Base):
    __tablename__ = "collaborators"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[Optional[str]] = mapped_column(unique=True, index=True)

    work_logs: Mapped[list["WorkLog"]] = relationship(back_populates="collaborator")


class WorkLog(Base):
    __tablename__ = "work_logs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    collaborator_id: Mapped[int] = mapped_column(ForeignKey("collaborators.id"))  # clé étrangère
    project: Mapped[str] = mapped_column(index=True)
    task: Mapped[str] = mapped_column()
    hours: Mapped[float] = mapped_column()
    date: Mapped[str] = mapped_column()
    status: Mapped[str] = mapped_column(default="En cours")
    description: Mapped[Optional[str]] = mapped_column()

    collaborator: Mapped["Collaborator"] = relationship(back_populates="work_logs")
