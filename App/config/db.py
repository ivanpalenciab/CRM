import os

from dotenv import load_dotenv
from sqlalchemy import create_engine,MetaData


meta = MetaData()

load_dotenv()

password = os.getenv("DATABASE_PASSWORD")
print(f"Esta es la contraseña {password}")
host = os.getenv("DATABASE_HOST")
database_name = os.getenv("DATABASE_NAME")
database_user = os.getenv("DATABASE_USER")
print(f"Esta es la contraseña {database_name}")

engine = create_engine(f"postgresql://{database_user}:{password}@{host}:5432/{database_name}")
conn = engine.connect()