from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'root'
passworld = 'prsthlrd99Erik'
host = 'localhost'
port = '3306'
db = 'fastAPI_SQLalchemy_fun_v1'

SQLALCHEMY_DATABASE_URL = f'mysql://{user}:{passworld}@{host}:{port}/{db}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
