import os

from dotenv import load_dotenv
from sqlalchemy import create_engine,MetaData


meta = MetaData()

load_dotenv()

password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_HOST")
database_name = os.getenv("DATABASE_NAME")
database_user = os.getenv("DATABASE_USER")

engine = create_engine(f"postgresql://{database_user}:{password}@{host}:5434/{database_name}")
conn = engine.connect()