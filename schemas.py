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

class UsuarioCreate(BaseModel):
    email: str
    password: str

class UsuarioResponse(BaseModel):
    id: int
    email: str
    class Config:
        from_attreibutes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str