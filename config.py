# Hidrobart Costeo
# Build : 101
# Version 1.0.101.0
# config.py  configuraciones

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///aihbcosteo.db")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
