# frontend/components/tbl_base_minimal.py

from nicegui import ui
import pandas as pd

def crear_tabla_minimal(nombre: str, columnas: list, data: pd.DataFrame):
    """Versión MÍNIMA sin row_key para test"""

    df = data.copy()

    ui.label(nombre).classes("text-xl font-bold mb-2")

    # Debug info
    with ui.card().classes("bg-green-100 p-2 mb-2"):
        ui.label(f"📊 Datos: {len(df)} filas x {len(df.columns)} columnas")
        ui.label(f"Columnas: {list(df.columns)}")

    # Tabla SIN row_key
    table = ui.table(columns=columnas, rows=df.to_dict('records'))

    ui.label(f"Mostrando {len(df)} registros")

    return table