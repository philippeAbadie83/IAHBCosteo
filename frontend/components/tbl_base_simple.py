# frontend/components/tbl_base_simple.py

from nicegui import ui
import pandas as pd

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

    # ======== Tabla básica ========
    with ui.card().classes("w-full shadow-md border border-gray-200 rounded-lg"):
        table = ui.table(
            columns=columnas,
            rows=[],  # ← Inicialmente vacío
            row_key=row_key,
        ).props(
            "pagination rows-per-page-options='10,25,50' rows-per-page=10"
        ).classes("h-[400px]")

    # ======== Función de actualización CORREGIDA ========
    def update_table():
        # 👇 VERIFICAR que el row_key existe y es único
        if row_key not in df.columns:
            ui.notify(f"❌ Columna '{row_key}' no encontrada. Columnas disponibles: {list(df.columns)}", type='negative')
            return

        # Verificar duplicados en el row_key
        if df[row_key].duplicated().any():
            duplicates = df[df[row_key].duplicated(keep=False)][row_key].unique()
            ui.notify(f"⚠️ Hay duplicados en '{row_key}': {duplicates}", type='warning')

        rows = df.to_dict(orient="records")
        table.rows = rows

        # Contador de registros
        result_text = f"Mostrando {len(rows)} de {len(df)} registros"
        if hasattr(update_table, 'result_count'):
            update_table.result_count.text = result_text
        else:
            with ui.row().classes("w-full justify-end mt-2"):
                update_table.result_count = ui.label(result_text)

    # 👇 AGREGAR DEBUG TEMPORAL
    with ui.card().classes("bg-blue-100 p-2 mb-2"):
        ui.label(f"🔍 DEBUG: row_key='{row_key}'")
        ui.label(f"Columnas del DataFrame: {list(df.columns)}")
        ui.label(f"Valores únicos en '{row_key}': {df[row_key].unique().tolist()}")
        ui.label(f"¿Hay duplicados?: {df[row_key].duplicated().any()}")

    update_table()

    return table
