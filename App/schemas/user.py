from datetime import date

from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    last_name:str
    contact_number:int
    identification_number: int
    gender: str
    email:str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    contact_number: Optional[str] = None
    identification_number: Optional[str] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    