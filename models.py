#Models de apipractica
from sqlalchemy import Column, Integer, String
from database import Base

class ProductoDB(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Integer)
    descripcion=Column(String, nullable=True)

class UsuarioDB(Base):
    __tablename__="usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email=Column(String, unique=True, index=True)
    hashed_password=Column(String)