# Hidrobart Costeo
# Build : 101
# Version 1.0.101.0
# core/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# Validar que la variable DATABASE_URL exista
if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definido en el archivo .env")

# Crear el engine con parámetros de conexión
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10
)

# Configurar la sesión
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_session():
    """Devuelve una sesión de base de datos lista para usar"""
    return SessionLocal()
