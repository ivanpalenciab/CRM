from datetime import date

from fastapi import APIRouter,HTTPException
from sqlalchemy import select,delete,update
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from models.user import users
from config.db import conn, engine
from schemas.user import UserCreate, UserUpdate

user = APIRouter()

@user.get("/users/")
def get_user():
    """
    This endpoint allows obtaining all users registered in the database.
    """
    try:
        stmt = select(users)
        result = conn.execute(stmt)

        users_list = []
        for row in result:
            user ={
                "id":row.id,
                "name":row.name,
                "last_name":row.last_name,
                "contact_number":row.contact_number,
                "identification_number":row.identification_number,
                "segment":row.segment,
                "gender":row.gender,
                "email":row.email,
                "last_order":row.last_order,
                "registration_date":row.registration_date
            }
            users_list.append(user)
        
        return users_list

    except Exception as e:
        return {"error": f"Error geting data: {str(e)}"}

@user.get("/user/{user_id}")
async def get_user(user_id):
    """
This endpoint allow you to get one user, You will need the user Id
"""
    query=select(users).where(users.c.id  == user_id)
    try:
        response = conn.execute(query)
        user=response.fetchone()

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        else:

            user_info = {
                "id":user[0],
                "name":user[1],
                "last_name":user[2],
                "contact_number":user[3],
                "identification_number":user[4],
                "segment":user[5],
                "gender":user[6],
                "email":user[7],
                "last_order":user[8],
                "registration_date":user[9]

            }

        return user_info
    except Exception as e:
        return {"error": f"Error processing user: {str(e)}"}
    
@user.post("/create-users/")
def create_user(user: UserCreate):
    """
This end point allow you to create an user 
"""
    new_user = users.insert().values(
        name=user.name,
        last_name=user.last_name,
        contact_number=user.contact_number,
        identification_number=user.identification_number,
        segment="New User",
        gender=user.gender,
        email=user.email,
        last_order = None,
        registration_date=date.today()
    )

    try:
        conn.execute(new_user)
        conn.commit()
        return {"message": "Usuario creado con éxito"}
    except SQLAlchemyError as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating the user: {str(e)}")
    
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {str(e)}")
        
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

@user.put("/user-update/{user_id}")
async def user_update(user_id: int, user_update: UserUpdate):
        """
       This endpoint alliw you to update an user  
        """
        query=select(users).where(users.c.id  == user_id)
        response = conn.execute(query)
        user=response.fetchone()

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        # data preparation for update
        update_data = user_update.dict(exclude_unset=True)

        # create query to update
        update_query = (
            update(users).where(users.c.id == user_id).values(**update_data))

    # Eexecute query
        conn.execute(update_query)
        conn.commit()

        return {"message": "User updated successfully"}

@user.delete("/delete-user/{user_id}")
async def delete_user(user_id):
    """
    this endpoint allow you to delete an user 
    """
    query=select(users).where(users.c.id  == user_id)
    response = conn.execute(query)
    user=response.fetchone()
    try:
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        conn.execute(users.delete().where(users.c.id == user_id))
        conn.commit()
        return {"Message":"User deleted"}
    except Exception as e:
       return {"error": f"Error processing user: {str(e)}"}