from fastapi import APIRouter, HTTPException
from sqlalchemy import select,delete,update
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError

from models.product import products
from config.db import conn
from schemas.product import ProductCreate
from schemas.product import ProductUpdate

product = APIRouter()

@product.get("/products/")
def get_products():
    """
    This endpoint allow us to get all products of the business
    """
    query = select(products)
    result = conn.execute(query)

    try:

        product_list = []

        for row in result:
            product={
                "id":row.id,
                "name":row.name,
                "description":row.description,
                "price":row.price,
                "stock":row.stock,
                "category":row.category,
                "brand":row.brand,
                "status":row.status
            }
            product_list.append(product)

        return product_list
    except Exception as e:
        return {"error": f"Error geting data: {str(e)}"}

@product.get("/product/{product_id}")
async def get_product(product_id):
    """
    This endpoint allow us to get one product for that you need to give the product id
    """
    query = select(products).where(products.c.id == product_id)
    try:
        response = conn.execute(query)
        product = response.fetchone()
        if product is None:
            raise HTTPException(status_code=404, detail="User not found")
            
        product_info = {
                "id":product[0],
                "name":product[1],
                "description":product[2],
                "price":product[3],
                "stock":product[4],
                "category":product[5],
                "brand":product[6],
                "status":product[7]
            }

        return product_info

    except Exception as e:
        return {"error": f"Error geting data: {str(e)}"}
    
@product.post("/product-create/")
async def create_product(product:ProductCreate):
    """This endpoint allow us to create a new product in database """
    new_product = products.insert().values(
        name = product.name,
        description = product.description,
        price = product.price,
        stock = product.stock,
        category = product.category,
        brand = product.brand,
        status = product.status
    )
    try:
        conn.execute(new_product)
        conn.commit()
        return {"Message":"Product created successfull"}
    except SQLAlchemyError as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating the user: {str(e)}")
    
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
        
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

@product.put("/product-update/{product_id}")
async def update_product(product_id, product_update:ProductUpdate):
    """
    Whit this endpoint you can update the product information
    """
    query = select(products).where(products.c.id == product_id)
    response = conn.execute(query)
    product = response.fetchone()
    
    try:
        if product is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        update_data = product_update.model_dump(exclude_unset=True)
        update_query = (
            update(products).where(products.c.id == product_id).values(**update_data))
        
        conn.execute(update_query)
        conn.commit()

        return{"message":"product updated successfully"}
    except Exception as e:
        return {"Error":"error procesing data{e}"}

@product.delete("/product-delete/{product_id}")
async def delete_product(product_id):
    """
    Here you can delete the product in database.
    """
    query = select(products).where(products.c.id == product_id)
    response = conn.execute(query)
    product=response.fetchone()

    try:
        if product is None:
            raise HTTPException(status_code=404, detail="User not found")
        conn.execute(products.delete().where(products.c.id==product_id))
        conn.commit()
        return {"Message":"product deleted"}
    except Exception as e:
       return {"error": f"Error processing product: {str(e)}"}