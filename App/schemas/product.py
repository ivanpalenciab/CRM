from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    description:str
    price:float
    stock: int
    category: str
    brand:str
    status:str

class ProductUpdate(BaseModel):
    name: Optional[str]=None
    description:Optional[str]=None
    price:Optional[int]=None
    stock: Optional[int]=None
    category: Optional[str]=None
    brand:Optional[str]=None
    status:Optional[str]=None