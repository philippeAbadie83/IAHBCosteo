# Hidrobart Costeo
# config.py  configuraciones

from core.__version__ import __version__, __build__
print(f"Versión: {__version__}, Build: {__build__}")

import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

# Variables de conexión
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
