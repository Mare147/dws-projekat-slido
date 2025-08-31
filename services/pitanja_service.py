from repositories import pitanja_repository
from models.pitanja_model import Pitanja
from fastapi import HTTPException
from schemas.pitanja_schema import PitanjeCreate, PitanjeUpdate
from sqlmodel import Session
from database import engine

def add_pitanje(session: Session, data: PitanjeCreate) -> Pitanja:
    pit = Pitanja(**data.dict())
    return pitanja_repository.create_pitanje(session, pit)

def list_pitanja(session: Session, offset: int = 0, limit: int = 100):
    return pitanja_repository.get_pitanja(session, offset, limit)

def get_pitanje(session: Session, pitanje_id: int) -> Pitanja:
    pit = pitanja_repository.get_pitanje(session, pitanje_id)
    if not pit:
        raise HTTPException(status_code=404, detail="Pitanje not found")
    return pit

def update_pitanje(session: Session, pitanje_id: int, data: PitanjeUpdate) -> Pitanja:
    pit = pitanja_repository.get_pitanje(session, pitanje_id)
    if not pit:
        raise HTTPException(status_code=404, detail="Pitanje not found")
    return pitanja_repository.update_pitanje(session, pit, data.dict(exclude_unset=True))

def delete_pitanje(session: Session, pitanje_id: int) -> None:
    pit = pitanja_repository.get_pitanje(session, pitanje_id)
    if not pit:
        raise HTTPException(status_code=404, detail="Pitanje not found")
    pitanja_repository.delete_pitanje(session, pit)
