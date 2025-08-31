from contextlib import asynccontextmanager
from typing import Annotated
from models.predavanje_model import Predavanje
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query, APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select
from schemas.predavanje_schema import PredavanjeRead, PredavanjeCreate, PredavanjeUpdate
from services import predavanje_service

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

@router.post("/", response_model=PredavanjeRead)
def create_predavanje(session: SessionDep, data: PredavanjeCreate):
    return predavanje_service.add_predavanje(session, data)

@router.get("/", response_model=list[PredavanjeRead])
def list_predavanja(session: SessionDep, offset: int = 0, limit: int = 100):
    return predavanje_service.list_predavanja(session, offset, limit)

@router.get("/{predavanje_id}", response_model=PredavanjeRead)
def get_predavanje(session: SessionDep, predavanje_id: int):
    pred = predavanje_service.get_predavanje(session, predavanje_id)
    if not pred:
        raise HTTPException(status_code=404, detail="Predavanje not found")
    return pred

@router.put("/{predavanje_id}", response_model=PredavanjeRead)
def update_predavanje(session: SessionDep, predavanje_id: int, data: PredavanjeUpdate):
    return predavanje_service.update_predavanje(session, predavanje_id, data)

@router.delete("/{predavanje_id}")
def delete_predavanje(session: SessionDep, predavanje_id: int):
    predavanje_service.delete_predavanje(session, predavanje_id)
    return {"message": "Predavanje obrisano"}
