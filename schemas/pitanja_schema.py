
from models.pitanja_model import Pitanja
from contextlib import asynccontextmanager
from typing import Annotated
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class PitanjeCreate(BaseModel):
    tekst: str
    predavanje_id: int
    autor_id: int

class PitanjeRead(BaseModel):
    id: int
    predavanje_id: int
    autor_id: int
    vrijeme: Optional[datetime]
    odobreno: bool
    odgovoreno: bool
    sakriveno: bool
    odgovor: Optional[str]
    vrijeme_odgovora: Optional[datetime]

    class Config:
        orm_mode = True

class PitanjeUpdate(BaseModel):
    tekst: str | None = None
    predavanje_id: int | None = None
    user_id: int | None = None