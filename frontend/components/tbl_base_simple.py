
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

    # ======== Contador FUERA de update_table ========
    with ui.row().classes("w-full justify-end mb-2"):
        result_count = ui.label("")  # ← Crear aquí, fuera de la función

    # ======== Tabla básica ========
    with ui.card().classes("w-full shadow-md border border-gray-200 rounded-lg"):
        table = ui.table(
            columns=columnas,
            rows=[],
            row_key=row_key,
        ).props(
            "pagination rows-per-page-options='10,25,50' rows-per-page=10"
        ).classes("h-[400px]")

    # ======== Función de actualización SIMPLIFICADA ========
    def update_table():
        rows = df.to_dict(orient="records")
        table.rows = rows
        # 👇 Actualizar contador SIN crear nuevos elementos UI
        result_count.text = f"Mostrando {len(rows)} de {len(df)} registros"

    update_table()  # Llamar una vez para inicializar

    return table
