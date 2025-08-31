from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class UserPitanje(SQLModel, table=True):
    user_id: int = Field(primary_key=True)
    pitanje_id: int = Field(primary_key=True)