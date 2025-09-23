# frontend/components/tbl_base_minimal.py

from nicegui import ui
import pandas as pd

def crear_tabla_minimal(
    nombre: str,
    columnas: list,
    data: pd.DataFrame,
    row_key: str = "id"
):
    """Versión MINIMALISTA sin actualizaciones dinámicas"""
    df = data.copy()

    if nombre:
        ui.label(nombre).classes("text-xl font-bold mb-2")

    # Convertir DataFrame a lista de diccionarios
    rows = df.to_dict(orient="records")

    # Crear contador simple
    ui.label(f"Mostrando {len(rows)} registros").classes("text-sm text-gray-600 mb-2")

    # Crear tabla directamente
    table = ui.table(columns=columnas, rows=rows, row_key=row_key).classes("w-full")

    return table