
from models.user_model import User
from contextlib import asynccontextmanager
from typing import Annotated
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class PredavanjeCreate(BaseModel):
    naziv: str
    kod: str
    predavac_id: int
    vrijeme: Optional[datetime]
    ponavljanje: Optional[str] = None
    cover_image: Optional[str] = None



class PredavanjeRead(BaseModel):
    id: int
    naziv: str
    kod: str
    predavac_id: int
    vrijeme: Optional[datetime]
    ponavljanje: Optional[str] 
    cover_image: str

    class Config:
        orm_mode = True


class PredavanjeUpdate(BaseModel):
    naziv: Optional[str] = None
    kod: Optional[str] = None
    predavac_id: Optional[int] = None
    vrijeme: Optional[datetime] = None 
    ponavljanje: Optional[str] = None
    cover_image: Optional[str] = None
