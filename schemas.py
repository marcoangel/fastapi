#schemas de apiprueba
from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    precio: int
    descripcion: Optional[str]=None
    
class ProductoResponse(ProductoBase):
    id: int
    class Config:
        from_attributes = True



