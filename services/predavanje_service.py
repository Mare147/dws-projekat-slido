from repositories import predavanje_repository
from models.predavanje_model import Predavanje
from fastapi import HTTPException
from schemas.predavanje_schema import PredavanjeCreate, PredavanjeUpdate
from sqlmodel import Session

def add_predavanje(session: Session, data: PredavanjeCreate) -> Predavanje:
    pred = Predavanje(**data.dict())
    return predavanje_repository.create_predavanje(session, pred)

def list_predavanja(session: Session, offset: int = 0, limit: int = 100):
    return predavanje_repository.get_predavanja(session, offset, limit)

def get_predavanje(session: Session, predavanje_id: int) -> Predavanje:
    pred = predavanje_repository.get_predavanje(session, predavanje_id)
    if not pred:
        raise HTTPException(status_code=404, detail="Predavanje not found")
    return pred

def update_predavanje(session: Session, predavanje_id: int, data: PredavanjeUpdate) -> Predavanje:
    pred = predavanje_repository.get_predavanje(session, predavanje_id)
    if not pred:
        raise HTTPException(status_code=404, detail="Predavanje not found")
    return predavanje_repository.update_predavanje(session, pred, data.dict(exclude_unset=True))

def delete_predavanje(session: Session, predavanje_id: int) -> None:
    pred = predavanje_repository.get_predavanje(session, predavanje_id)
    if not pred:
        raise HTTPException(status_code=404, detail="Predavanje not found")
    predavanje_repository.delete_predavanje(session, pred)
