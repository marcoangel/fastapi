#Router apiprueba
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import ProductoDB
from schemas import ProductoBase, ProductoResponse

# Creamos el router en lugar de usar @app
router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("", response_model=List[ProductoResponse])
def obtener_productos(db: Session = Depends(get_db)):
    return db.query(ProductoDB).all()

@router.post("", response_model=ProductoResponse, status_code=201)
def crear_producto(producto: ProductoBase, db: Session = Depends(get_db)):
    nuevo = ProductoDB(**producto.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(ProductoDB).filter(ProductoDB.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.delete("/{producto_id}", response_model=ProductoResponse)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(ProductoDB).filter(ProductoDB.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return producto