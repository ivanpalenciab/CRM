from datetime import date

from sqlalchemy import Table, Column, func
from sqlalchemy.sql.sqltypes import Integer, String,Date,BigInteger

from App.config.db import meta, engine

users = Table("users",meta, 
        Column("id",Integer, primary_key=True), 
        Column("name", String),
        Column("last_name", String),
        Column("contact_number", BigInteger),
        Column("identification_number", BigInteger),
        Column("segment",String,default="New User"),
        Column("gender",String),
        Column("email",String),
        Column("last_order",Date),
        Column("registration_date",Date, default=func.current_date()))

meta.create_all(engine)
