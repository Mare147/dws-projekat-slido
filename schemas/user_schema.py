
from models.user_model import User
from contextlib import asynccontextmanager
from typing import Annotated
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str


class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    password: str
    blocked_until: Optional[datetime]
    
    class Config:
        orm_mode = True
    
class UserUpdate(BaseModel):
    username: str|None 
    email: EmailStr|None

  