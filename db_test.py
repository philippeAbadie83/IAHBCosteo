# Hidrobart Costeo
# Build : 101
# Version 1.0.101.0
# db_test.py

from core.db import get_session
from sqlalchemy import text

def main():
    session = get_session()
    try:
        # Usar sqlalchemy.text en lugar de string directo
        result = session.execute(text("SELECT NOW()")).fetchone()
        print("✅ Conexión exitosa:", result)
    finally:
        session.close()

if __name__ == "__main__":
    main()
