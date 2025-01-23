from fastapi import FastAPI

from routes.user import user
from routes.product import product
from routes.order import order
from routes.order_product import order_product


app = FastAPI()
app.include_router(user)
app.include_router(product)
app.include_router(order)
app.include_router(order_product)