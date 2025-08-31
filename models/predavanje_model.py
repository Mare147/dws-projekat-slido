from sqlmodel import SQLModel, Field
from typing import Optional

from datetime import datetime

class Predavanje(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    naziv: str
    kod: str
    predavac_id: int
    vrijeme: Optional[datetime]
    ponavljanje: Optional[str] = None
    cover_image: Optional[str] = None

