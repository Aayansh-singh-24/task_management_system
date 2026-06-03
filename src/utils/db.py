from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.setting import setting

Base = declarative_base() # use to mapped python class with database and help in table creation

engine = create_engine(url = setting.DB_CONNECTION) # engine = main connection system with database

sessionLocal = sessionmaker(bind=engine) # create a temporary active conversation with databse

def get_db():
    session = sessionLocal()
    try:
        yield session
    finally:
        session.close()