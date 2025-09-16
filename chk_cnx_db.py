from core.db import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        version = conn.execute(text("SELECT VERSION()")).scalar()
        print("✅ Conexión OK, versión MySQL:", version)
except Exception as e:
    print("❌ Error de conexión:", e)
