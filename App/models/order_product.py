from sqlalchemy import Table,Column,ForeignKey
from sqlalchemy.sql.sqltypes import Integer,Numeric

from App.config.db import meta, engine
from App.models.order import orders
from App.models.product import products

orders_products = Table("order_product",meta,
                        Column("id",Integer,primary_key=True),
                        Column("order_id",Integer,ForeignKey("orders.id",ondelete="CASCADE")),
                        Column("product_id",Integer,ForeignKey("product.id")),
                        Column("amount",Integer),
                        Column("unit_price",Numeric(precision=10,scale=2)),
                        Column("subtotal",Numeric(precision=10,scale=2))

)

meta.create_all(engine)