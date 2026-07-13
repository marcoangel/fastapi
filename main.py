#Main de apiprueba
from fastapi import FastAPI
import models
from database import engine
from productos_router import router

# Creamos las tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Profesional Modularizada")

# Incluimos las rutas del archivo independiente
app.include_router(router)

print("holamundo")