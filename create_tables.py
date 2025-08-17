# create_tables.py
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.models import Base  # Import Base from your models module

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

print("Creating database tables...")
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
