import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


# DATABASE_HOSTNAME = os.environ["DATABASE_HOSTNAME"]
# DATABASE_PORT = os.environ["DATABASE_PORT"]
# DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
# DATABASE_NAME = os.environ["DATABASE_NAME"]
# DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]

DATABASE_URL = os.environ.get("DATABASE_URL")
# SQLALCHEMY_DATABASE_URL = f'postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE_NAME}'
# postgresql://databasepostgres_hagz_user:l3q6yH5wuoaSLjx4jrRXCeOBaAREOULT@dpg-ckrrumo1hnes738ub1ug-a/databasepostgres_hagz

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()