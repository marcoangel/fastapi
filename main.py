#Main de apiprueba
from fastapi import FastAPI
import models
from database import engine
from productos_router import router as productos_router
from usuarios_router import router as usuarios_router

# Creamos las tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Profesional Modularizada")

# Incluimos las rutas del archivo independiente
app.include_router(productos_router)
app.include_router(usuarios_router)