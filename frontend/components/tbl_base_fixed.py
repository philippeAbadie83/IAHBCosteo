# frontend/components/tbl_base_fixed.py

from nicegui import ui
import pandas as pd

def crear_tabla_fixed(
    nombre: str,
    columnas: list,
    data: pd.DataFrame,
    row_key: str = "id"
):
    """Versión FIXED - Características básicas solamente"""
    df = data.copy()

    # 1. Título simple
    if nombre:
        ui.label(nombre).classes("text-2xl font-bold mb-4")

    # 2. Contador SEPARADO
    result_label = ui.label("").classes("text-sm text-gray-600 mb-2")

    # 3. Tabla básica
    with ui.card().classes("w-full border rounded-lg"):
        table = ui.table(
            columns=columnas,
            rows=[],
            row_key=row_key,
        ).props("pagination rows-per-page=25").classes("h-[500px]")

    # 4. Actualización SIMPLE
    def update_table():
        rows = df.to_dict(orient="records")
        table.rows = rows
        result_label.text = f"Mostrando {len(rows)} de {len(df)} registros"

    update_table()

    return table