# Hidrobart Costeo
# Build : 101
# Version 1.0.101.0
# config.py  configuraciones

import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

# Variables de conexión
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
