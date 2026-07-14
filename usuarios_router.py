#usuarios puter
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import UsuarioDB
from schemas import UsuarioCreate, UsuarioResponse, TokenResponse
from passlib.context import CryptContext
import bcrypt # 🔽 Importamos bcrypt directamente
import jwt # 🔽 Importamos PyJWT
from datetime import datetime, timedelta, timezone

SECRET_KEY = "mi_clave_secreta_super_segura_para_el_remoto"
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth", tags=["Autenticación"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/registro", response_model=UsuarioResponse, status_code=201)
def resgistroUsuario(usuario: UsuarioCreate, db:Session=Depends(get_db)):
    existe=db.query(UsuarioDB).filter(UsuarioDB.email==usuario.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="El email ya esta registrado")
    #password_cifrada = pwd_context.hash(usuario.password)

    password_bytes = usuario.password.encode('utf-8')
    sal = bcrypt.gensalt() # Genera una semilla de seguridad aleatoria
    password_cifrada = bcrypt.hashpw(password_bytes, sal)

    nuevo_usuario = UsuarioDB(email=usuario.email, hashed_password=password_cifrada.decode('utf-8'))
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return nuevo_usuario

@router.get("/", response_model=List[UsuarioResponse])
def obtenerUsuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioDB).all()


@router.post("/login", response_model=TokenResponse)
def login(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_db = db.query(UsuarioDB).filter(UsuarioDB.email == usuario.email).first()
    if not usuario_db:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    # Verificar la contraseña usando bcrypt
    password_bytes = usuario.password.encode('utf-8')
    hashed_password_bytes = usuario_db.hashed_password.encode('utf-8')
    
    if not bcrypt.checkpw(password_bytes, hashed_password_bytes):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    # Generar token JWT
    expiration = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload = {
        "sub": usuario_db.email,
        "exp": expiration.timestamp()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": token, "token_type": "bearer"}