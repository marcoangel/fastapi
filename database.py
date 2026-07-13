#Data base apiprueba
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABSE_URL = "sqlite:///./inventario.db"
engine = create_engine(DATABSE_URL, connect_args={"check_same_thread":False})
SessionLocal= sessionmaker(autocommit = False, autoflush = False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()