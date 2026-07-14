# 🚀 API de Gestión de Inventario & Autenticación Segura

Este es un proyecto backend robusto desarrollado en Python utilizando **FastAPI**. Implementa un sistema completo de administración de productos (CRUD) con persistencia de datos en una base de datos relacional y un módulo de seguridad avanzado para el registro e inicio de sesión de usuarios mediante tokens **JWT**.

Diseñado bajo estándares de arquitectura limpia, modularización y buenas prácticas exigidas en entornos de desarrollo remoto internacional.

---

## 🛠️ Tecnologías y Ecosistema

* **Framework:** FastAPI (Python 3.10+)
* **Base de Datos:** SQLite (Motor ligero relacional)
* **ORM (Mapeo Objeto-Relacional):** SQLAlchemy
* **Seguridad y Cifrado:** Bcrypt (Cifrado de contraseñas) & PyJWT (JSON Web Tokens)
* **Validación de Datos:** Pydantic

---

## 📂 Arquitectura y Estructura del Proyecto

El código está completamente modularizado siguiendo el principio de **Separación de Responsabilidades**, facilitando la escalabilidad y el mantenimiento:

* `main.py`: Punto de entrada de la aplicación. Inicializa FastAPI e incluye las rutas.
* `database.py`: Configura la conexión a la base de datos SQLite y gestiona el ciclo de vida de las sesiones (`get_db`).
* `models.py`: Define las tablas y la estructura de los datos en la base de datos usando SQLAlchemy.
* `schemas.py`: Contiene los modelos de Pydantic que validan las peticiones del cliente y filtran las respuestas del servidor.
* `productos_router.py`: Endpoints y lógica de negocio para la gestión del inventario.
* `usuarios_router.py`: Endpoints para el registro de usuarios (hashing) y autenticación (Login/JWT).

---

## 🛣️ Endpoints Disponibles

### 🔐 Módulo de Autenticación (`/auth`)
* `POST /auth/registro` - Registra un nuevo usuario. Aplica *hashing* seguro a la contraseña antes de guardarla.
* `POST /auth/login` - Valida las credenciales del usuario y genera un Token de Acceso (JWT) firmado con algoritmo `HS256` válido por 2 horas.

### 📦 Módulo de Productos (`/productos`)
* `GET /productos` - Recupera la lista completa de artículos en el inventario.
* `GET /productos/{id}` - Busca un artículo específico por su ID (Retorna `404 Not Found` si no existe).
* `POST /productos` - Registra un nuevo artículo validando estrictamente los tipos de datos recibidos.
* `PUT /productos/{id}` - Modifica todos los campos de un artículo existente.
* `DELETE /productos/{id}` - Elimina físicamente un artículo de la base de datos por su ID.

---

## 💻 Instalación y Ejecución Local

Sigue estos pasos para levantar el entorno de desarrollo en tu máquina local:

### 1. Clonar el repositorio
```bash
git clone github@marcoangel/fastapi
cd fastapi