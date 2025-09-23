
# frontend/components/tbl_base_simple.py

from nicegui import ui
import pandas as pd
from typing import List, Dict

def crear_tabla_simple(
    nombre: str,
    columnas: list,
    data: pd.DataFrame,
    row_key: str = "id"
):
    df = data.copy()

    # ======== Título simple ========
    if nombre:
        ui.label(nombre).classes("text-2xl font-bold text-gray-800 mb-4")

    # ======== DEBUG INFO ========
    with ui.card().classes("bg-yellow-100 p-2 mb-2"):
        ui.label(f"🔍 DEBUG: row_key='{row_key}'")
        ui.label(f"Columnas: {list(df.columns)}")
        ui.label(f"Registros: {len(df)}")
        ui.label(f"Valores únicos en '{row_key}': {df[row_key].unique().tolist()}")

    # ======== CONVERTIR DATOS ANTES de crear la tabla ========
    rows = df.to_dict(orient="records")

    # ======== Crear tabla con los datos DIRECTAMENTE ========
    with ui.card().classes("w-full shadow-md border border-gray-200 rounded-lg"):
        table = ui.table(
            columns=columnas,
            rows=rows,  # 👈 Pasar datos DIRECTAMENTE aquí
            row_key=row_key,
        ).props(
            "pagination rows-per-page-options='10,25,50' rows-per-page=10"
        ).classes("h-[400px]")

    # ======== Contador de registros ========
    with ui.row().classes("w-full justify-end mt-2"):
        ui.label(f"Mostrando {len(rows)} de {len(df)} registros")

    return table