# frontend/components/tbl_base_simple.py

from nicegui import ui
import pandas as pd


def crear_tabla_simple(
    nombre: str,
    columnas: list,
    data: pd.DataFrame,
    row_key: str = "id"  # 👈 Hacemos row_key configurable
):
    """
    Versión SIMPLIFICADA de tbl_base para debugging
    """
    df = data.copy()

    # ======== Título simple ========
    if nombre:
        ui.label(nombre).classes("text-2xl font-bold text-gray-800 mb-4")

    # ======== Tabla básica ========
    with ui.card().classes("w-full shadow-md border border-gray-200 rounded-lg"):
        table = ui.table(
            columns=columnas,
            rows=[],
            row_key=row_key,  # 👈 Usamos el parámetro configurable
        ).props(
            "pagination rows-per-page-options='10,25,50' rows-per-page=10"
        ).classes("h-[400px]")

    # ======== Función de actualización ========
    def update_table():
        rows = df.to_dict(orient="records")
        table.rows = rows

        # Contador de registros
        result_text = f"Mostrando {len(rows)} de {len(df)} registros"
        if hasattr(update_table, 'result_count'):
            update_table.result_count.text = result_text
        else:
            with ui.row().classes("w-full justify-end mt-2"):
                update_table.result_count = ui.label(result_text)

    update_table()

    return table