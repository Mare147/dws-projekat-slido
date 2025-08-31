from sqlmodel import SQLModel, Field
from typing import Optional

from datetime import datetime


class UserPredavanje(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    predavanje_id: int = Field(foreign_key="predavanje.id")
    ocjena: float