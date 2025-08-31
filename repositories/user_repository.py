from models.user_model import User
from contextlib import asynccontextmanager
from typing import Annotated
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
from schemas.user_schema import UserCreate, UserUpdate, UserRead


def create_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_users(session: Session, offset: int = 0, limit: int = 100) -> list[User]:
    return session.exec(select(User).offset(offset).limit(limit)).all()

def get_user(session: Session, user_id: int) -> User|None:
    return session.get(User, user_id)

def update_user(session: Session, db_user: User, updates: dict) -> User:
    for key, value in updates.items():
        setattr(db_user, key, value)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    
def delete_user(session: Session, db_user: User) -> None:
    session.delete(db_user)
    session.commit()

    