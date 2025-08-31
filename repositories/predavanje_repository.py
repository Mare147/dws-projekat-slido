from models.predavanje_model import Predavanje
from contextlib import asynccontextmanager
from typing import Annotated
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from schemas.predavanje_schema import PredavanjeCreate, PredavanjeRead, PredavanjeUpdate


def create_predavanje(session: Session, predavanje: Predavanje) -> Predavanje:
    session.add(predavanje)
    session.commit()
    session.refresh(predavanje)
    return predavanje

def get_predavanja(session: Session, offset: int = 0, limit: int = 100) -> list[Predavanje]:
    return session.exec(select(Predavanje).offset(offset).limit(limit)).all()

def get_predavanje(session: Session, predavanje_id: int) -> Predavanje|None:
    return session.get(Predavanje, predavanje_id)

def update_predavanje(session: Session, db_predavanje: Predavanje, updates: dict) -> Predavanje:
    for key, value in updates.items():
        setattr(db_predavanje, key, value)
    session.add(db_predavanje)
    session.commit()
    session.refresh(db_predavanje)
    return db_predavanje

def delete_predavanje(session: Session, db_predavanje: Predavanje) -> None:
    session.delete(db_predavanje)
    session.commit()
