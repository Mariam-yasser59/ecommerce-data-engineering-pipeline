import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


# Load environment variables
load_dotenv()


# Read database configuration
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# Create PostgreSQL connection
DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


# Test connection
try:
    with engine.connect() as connection:
        print("PostgreSQL connection successful!")

except Exception as e:
    print("Database connection failed!")
    print(e)