from pydantic import BaseModel
from typing import Optional

class CreateOrderDetail(BaseModel):
    order_id:int
    product_id:int
    amount:int

class UpdateOrderDetail(BaseModel):
    order_id:Optional[int]=None
    product_id:Optional[int]=None
    amount:Optional[int]=None