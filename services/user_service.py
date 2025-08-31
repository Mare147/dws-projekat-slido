from repositories import user_repository
from models.user_model import User
from contextlib import asynccontextmanager
from typing import Annotated
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

from schemas.user_schema import UserCreate, UserUpdate, UserRead

def create_user(session: Session, user_data: UserCreate) -> User:
    user = User(**user_data.dict())
    return user_repository.create_user(session, user)

def get_users(session: Session, offset: int = 0, limit: int = 100) -> list[User]:
    return user_repository.get_users(session, offset, limit)

def get_user(session: Session, user_id: int) -> User:
    user = user_repository.get_user(session, user_id)
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found")
    return user

def update_user(session: Session, user_id: int, user_data: UserUpdate) -> User:
    db_user = user_repository.get_user(session, user_id)
    if not db_user:
        raise HTTPException(status_code = 404, detail = "User not found")
    return user_repository.update_user(session, db_user, user_data.dict(exclude_unset=True))

def delete_user(session: Session, user_id: int) -> None:
    db_user = user_repository.get_user(session, user_id)
    if not db_user:
        raise HTTPException(status_code = 404, detail = "User not found")
    user_repository.delete_user(session, db_user)
    