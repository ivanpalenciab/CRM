from sqlalchemy import Table, Column, func
from sqlalchemy.sql.sqltypes import Integer, String,Date,Numeric

from App.config.db import meta, engine

products = Table("product",meta, 
        Column("id",Integer, primary_key=True), 
        Column("name", String),
        Column("description", String),
        Column("price", Numeric(precision=10, scale=2)),
        Column("stock", String),
        Column("category",String),
        Column("brand",String),
        Column("status",String),)

meta.create_all(engine)