from fastapi import APIRouter, HTTPException
from sqlalchemy import select,delete,update
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from schemas.order_product import CreateOrderDetail,UpdateOrderDetail
from models.order_product import orders_products
from models.product import products
from models.order import orders
from config.db import conn

order_product = APIRouter()
@order_product.get("/detail/{detail_id}")
async def get_detail(detail_id):
    """
    This endpoint allows me to access the information of each detail by providing the detail ID.
    """
    try:
        query = orders_products.select().where(orders_products.c.id==detail_id)
        result = conn.execute(query)
        detail = result.fetchone()

        if detail is None:
            raise HTTPException(status_code=404, detail="detail not exist")

        detail_info = {
            "id":detail[0],
            "order_id":detail[1],
            "product_id":detail[2],
            "amount":detail[3],
            "unit_price":detail[4],
            "subtotal":detail[5]
        }
        return detail_info

    except Exception as e:
        return {"error": f"Error geting data: {str(e)}"}
    
@order_product.get("/order-details/{order_id}")
async def get_order_details(order_id):
    """
    This endpoint allows me to access all the details associated with an order; the order ID must be provided.
    """
    try:
        query = orders_products.select().where(orders_products.c.order_id==order_id)
        result = conn.execute(query)
        details = result.fetchall()

        order_details=[]

        for row in details:
            order_detail={
                    "id":row.id,
                    "order_id":row.order_id,
                    "product_id":row.product_id,
                    "amount":row.amount,
                    "unit_price":row.unit_price,
                    "subtotal":row.subtotal
                }
            order_details.append(order_detail)

        return order_details


    except Exception as e:
        return {"error": f"Error geting data: {str(e)}"}

@order_product.post("/detail-create/")
async def create_order_detail(order_detail:CreateOrderDetail):
    """
    This endpoint allow you to create a detail for a order.
    a detail is information about the product buyed and amount of it
    """
    try:
        query= select(products).where(products.c.id==order_detail.product_id)
        result = conn.execute(query)
        product=result.fetchone()
        if product is None:
            raise HTTPException(status_code=404, detail="product not found")
        else:
            unit_price = product[3]

        query_order = select(orders).where(orders.c.id==order_detail.order_id)
        result = conn.execute(query_order)
        order = result.fetchone()
        if order is None:
            raise HTTPException(status_code=404, detail="order not found")
        
        current_total = order[3]
        
        subtotal = order_detail.amount*unit_price

        new_order_detail = orders_products.insert().values(
            order_id=order_detail.order_id,
            product_id=order_detail.product_id,
            amount=order_detail.amount,
            unit_price=unit_price,
            subtotal=subtotal
        )
        conn.execute(new_order_detail)
        conn.commit()

        
        total_actualitation = current_total+subtotal
        update_total = update(orders).where(
            orders.c.id==order_detail.order_id).values(total=total_actualitation )
        conn.execute(update_total)
        conn.commit()

        
        return {"Message":"Detail created succesfully"}
    except SQLAlchemyError as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating the detail: {str(e)}")
    
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
        
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")
@order_product.put("/detail-update/{detail_id}",include_in_schema=False)
async def detail_update(detail_id:str,update_info:UpdateOrderDetail):
    """This endpoint allow us to update the details"""
    try:
        pass
    except SQLAlchemyError as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating the detail: {str(e)}")
    
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
        
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

@order_product.delete("/detail-delete/{detail_id}")
async def detail_delete(detail_id):
    """
    This endpoint allow you to delete a detail for a order
    """
    try:
        query = select(orders_products).where(orders_products.c.id==detail_id)
        result = conn.execute(query)
        detail = result.fetchone()

        order_id=detail[1]
        subtotal=detail[5]

        order_query = select(orders).where(orders.c.id == order_id)
        result_order = conn.execute(order_query)
        order = result_order.fetchone()

        total = order[3]
        new_total = total-subtotal

        delete_query = orders_products.delete().where(orders_products.c.id==detail_id)
        conn.execute(delete_query)
        conn.commit()

        update_query = update(orders).where(
            orders.c.id==order_id).values(total=new_total)
        conn.execute(update_query)
        conn.commit()



        return {"Message":"order detail deleted succefully"}

    except Exception as e:
        return {"Error":f"procesing error {e}"}