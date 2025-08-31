from sqlmodel import SQLModel, Field
from typing import Optional

from datetime import datetime



class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str 
    password: str 
    role: str  
    email: str
    blocked_until: Optional[datetime]  #ChatGPT
