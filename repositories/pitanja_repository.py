from models.pitanja_model import Pitanja
from contextlib import asynccontextmanager
from typing import Annotated
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from schemas.pitanja_schema import PitanjeCreate, PitanjeRead, PitanjeUpdate

def create_pitanja(session: Session, pitanje: Pitanja) -> Pitanja:
    session.add(pitanje)
    session.commit()
    session.refresh(pitanje)
    return pitanje

def get_pitanja(session: Session, offset: int = 0, limit: int = 100) -> list[Pitanja]:
    return session.exec(select(Pitanja).offset(offset).limit(limit)).all()

def get_pitanje(session: Session, pitanje_id: int) -> Pitanja|None:
    return session.get(Pitanja, pitanje_id)

def update_pitanje(session: Session, db_pitanje: Pitanja, updates: dict) -> Pitanja:
    for key, value in updates.items():
        setattr(db_pitanje, key, value)
    session.add(db_pitanje)
    session.commit()
    session.refresh(db_pitanje)
    return db_pitanje

def delete_pitanje(session: Session, db_pitanje: Pitanja) -> None:
    session.delete(db_pitanje)
    session.commit()
