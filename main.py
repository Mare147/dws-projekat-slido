from contextlib import asynccontextmanager
from typing import Annotated
from models.user_model import User
from database import engine
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

from controllers import user_controller, predavanje_controller, pitanja_controller, user_predavanje_controller
from fastapi.middleware.cors import CORSMiddleware
from schemas.user_schema import UserCreate, UserRead, UserUpdate

@asynccontextmanager
async def lifespan(app: FastAPI):
  create_db_and_tables()
  yield
  print("Gašenje aplikacije")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def index():
    return {"message": "Slido backend radi "}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
      "http://localhost:3000",
      "http://127.0.0.1:3000", 
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_db_and_tables():
  SQLModel.metadata.create_all(engine)

def get_session():
  with Session(engine) as session:
    yield session


SessionDep = Annotated[Session, Depends(get_session)]

app.include_router(user_controller.router, prefix="/users", tags=["Users"])
app.include_router(predavanje_controller.router, prefix="/predavanja", tags=["Predavanja"])
app.include_router(pitanja_controller.router, prefix="/pitanja", tags=["Pitanja"])
