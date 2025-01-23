from datetime import date

from pydantic import BaseModel
from typing import Optional

class CreateOrder(BaseModel):
    user_id:Optional[int]=None
    order_date:date
    order_status:str
    payment_method:str
    shipping_address:Optional[str]
    status:Optional[str]=None
    notes:Optional[str]=None
    shiping_date:Optional[date] = None
    delivery_date:Optional[date]=None

class UpdateOrder(BaseModel):
    user_id:Optional[int]=None
    order_date:Optional[date]=None
    order_status:Optional[str]=None
    payment_method:Optional[str]=None
    shipping_address:Optional[str]=None
    status:Optional[str]=None
    notes:Optional[str]=None
    shiping_date:Optional[date] = None
    delivery_date:Optional[date]=None


