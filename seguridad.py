from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError

SECRET_KEY = "mi_clave_secreta_super_segura_para_el_remoto"
ALGORITHM = "HS256"

# Una única instancia del candado para todo el sistema
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def obternerUsuarioActual(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return email
    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )