from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime



class Pitanja(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tekst: str
    predavanje_id: int
    autor_id: int
    vrijeme: Optional[datetime]
    odobreno: bool 
    odgovoreno: bool 
    sakriveno: bool
    broj_lajkova: int
    odgovor: str 
    vrijeme_odgovora: Optional[datetime]