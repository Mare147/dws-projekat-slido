from contextlib import asynccontextmanager
from typing import Annotated
from models.pitanja_model import Pitanja
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query, APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select
from schemas.pitanja_schema import PitanjeRead, PitanjeCreate, PitanjeUpdate
from services import pitanja_service

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

@router.post("/", response_model=PitanjeRead)
def create_pitanje(session: SessionDep, data: PitanjeCreate):
    return pitanja_service.add_pitanje(session, data)

@router.get("/", response_model=list[PitanjeRead])
def list_pitanja(session: SessionDep, offset: int = 0, limit: int = 100):
    return pitanja_service.list_pitanja(session, offset, limit)

@router.get("/{pitanje_id}", response_model=PitanjeRead)
def get_pitanje(session: SessionDep, pitanje_id: int):
    return pitanja_service.get_pitanje(session, pitanje_id)

@router.put("/{pitanje_id}", response_model=PitanjeRead)
def update_pitanje(session: SessionDep, pitanje_id: int, data: PitanjeUpdate):
    return pitanja_service.update_pitanje(session, pitanje_id, data)

@router.delete("/{pitanje_id}")
def delete_pitanje(session: SessionDep, pitanje_id: int):
    pitanja_service.delete_pitanje(session, pitanje_id)
    return {"message": "Pitanje obrisano"}
