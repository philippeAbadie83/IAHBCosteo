# core/db.py

from core.__version__ import __version__, __build__
print(f"Versión: {__version__}, Build: {__build__}")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 🔹 Cadena de conexión directa (sin depender de .env)
DATABASE_URL = "mysql+pymysql://hidroAdm@hidrobart-mysqlsrv:$Orozc4$olav%7867@hidrobart-mysqlsrv.mysql.database.azure.com:3306/hidrobart_costeo"

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
