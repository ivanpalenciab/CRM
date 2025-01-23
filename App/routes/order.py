from fastapi import APIRouter, HTTPException
from sqlalchemy import select,delete,update
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError

from models.order import orders
from config.db import conn
from schemas.order import CreateOrder,UpdateOrder

order = APIRouter()

@order.get("/orders/")
def get_orders():
    """This endpoint allow you to get info about all orders"""
    query = select(orders)
    result=conn.execute(query)

    try:
        orders_list=[]

        for row in result:
            order_info={
                "id":row.id,
                "user_id":row.user_id,
                "order_date":row.order_date,
                "total":row.total,
                "order_status":row.order_status,
                "payment_method":row.payment_method,
                "shipping_address":row.shipping_address,
                "status":row.status,
                "notes":row.notes,
                "shiping_date":row.shiping_date,
                "delivery_date":row.delivery_date

            }
            orders_list.append(order_info)
            

        return orders_list
    except Exception as e:
        return {"Error":f"error geting data{str(e)}"}

@order.get("/order/{order_id}")
async def get_order(order_id):
    """This endpoint allow you to get info about one order"""
    try:
        query = select(orders).where(orders.c.id==order_id)
        result = conn.execute(query)
        order = result.fetchone()
        if order is None:
            raise HTTPException(status_code=404, detail="order not exist")
        order_info={
             "id":order[0],
                "user_id":order[1],
                "order_date":order[2],
                "total":order[3],
                "order_status":order[4],
                "payment_method":order[5],
                "shipping_address":order[6],
                "status":order[7],
                "notes":order[8],
                "shiping_date":order[9],
                "delivery_date":order[10]
        }
        return order_info

    except Exception as e:
        return {"Error": "error getting data{e}"}
    
@order.post("/order-create/")
def order_create(order_info:CreateOrder):
    """This endpoint allow you to create a new order"""
    new_order = orders.insert().values(
        user_id=order_info.user_id,
        order_date=order_info.order_date,
        total=0,
        order_status=order_info.order_status,
        payment_method=order_info.payment_method,
        shipping_address=order_info.shipping_address,
        status=order_info.status,
        notes=order_info.notes,
        shiping_date=order_info.shiping_date,
        delivery_date=order_info.delivery_date
    )
    try:
        conn.execute(new_order)
        conn.commit()
        return {"message":"order created succesfully"}
    except SQLAlchemyError as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating the order: {str(e)}")
    
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
        
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")
    
@order.put("/order-update/{order_id}")
async def update_order(order_id,order_update:UpdateOrder):
    """This enpoint allow you to update a order, you have to give the order id"""
    try:
        query = select(orders).where(orders.c.id==order_id)
        result = conn.execute(query)
        order = result.fetchone()
        if order is None:
            raise HTTPException(status_code=404, detail="order not found")
        update_data= order_update.model_dump(exclude_unset=True)
        update_query = (
        update(orders).where(orders.c.id==order_id).values(**update_data))
        conn.execute(update_query)
        conn.commit()

        return {"message: order updated succesfully"}
        
    except Exception as e:
        return {"Error":f"error procesing data {e}"}
    
@order.delete("/oreder-delete/{order_id}")
async def order_delete(order_id):
    """This enpoint allow you to delete a order, you have to give the order id"""
    try:
        query = select(orders).where(orders.c.id==order_id)
        result = conn.execute(query)
        order = result.fetchone()
        if order is None:
            raise HTTPException(status_code=404, detail="order not found")
        conn.execute(orders.delete().where(orders.c.id==order_id))
        conn.commit()
        return {"Message": "order deleted successfully"}
    except Exception as e:
        return {"error": f"Error processing order: {str(e)}"}
    