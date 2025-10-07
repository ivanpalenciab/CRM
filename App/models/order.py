from sqlalchemy import Table, Column,ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String,Date,Numeric

from App.config.db import meta, engine
from App.models.user import users

orders = Table("orders",meta, 
        Column("id",Integer, primary_key=True), 
        Column("user_id", Integer,ForeignKey("users.id")),
        Column("order_date", Date),
        Column("total", Numeric(precision=10, scale=2)),
        Column("order_status", String),
        Column("payment_method",String),
        Column("shipping_address",String),
        Column("status",String),
        Column("notes",String),
        Column("shiping_date",Date),
        Column("delivery_date",Date))

meta.create_all(engine)