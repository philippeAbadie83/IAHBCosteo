# core/db.py
from core.__version__ import __version__, __build__
print(f"Versión: {__version__}, Build: {__build__}")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 🔹 Credenciales directas (hardcodeadas)
username = "hidroAdm"
password = "$Orozc4$olav%7867"   # la contraseña tal cual
host = "hidrobart-mysqlsrv.mysql.database.azure.com"
database = "hidrobart_costeo"

# 🔹 URL directa sin quote_plus ni nada
DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}:3306/{database}"

# Crear engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    future=True
)

# Configurar sesión
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_session():
    """Devuelve una sesión de base de datos lista para usar"""
    return SessionLocal()
