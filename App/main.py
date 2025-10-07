from fastapi import FastAPI

from App.routes.user import user
from App.routes.product import product
from App.routes.order import order
from App.routes.order_product import order_product


app = FastAPI()
app.include_router(user)
app.include_router(product)
app.include_router(order)
app.include_router(order_product)