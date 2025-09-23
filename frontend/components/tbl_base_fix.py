# frontend/components/tbl_base_fix.py

from nicegui import ui
import pandas as pd

def crear_tabla_fix(
    nombre: str,
    columnas: list,
    data: pd.DataFrame,
    row_key: str = "id"
):
    """Versión corregida del problema de actualización de filas"""

    df = data.copy()

    # Verificar que row_key existe
    if row_key not in df.columns:
        ui.notify(f"❌ Error: columna '{row_key}' no encontrada", type='negative')
        # Usar primera columna como fallback
        row_key = df.columns[0] if len(df.columns) > 0 else 'id'

    # Convertir a filas
    rows = df.to_dict('records')

    # Título
    if nombre:
        ui.label(nombre).classes("text-2xl font-bold mb-4")

    # DEBUG
    with ui.card().classes("bg-blue-100 p-2 mb-2"):
        ui.label(f"🚀 Tabla con {len(rows)} filas")
        ui.label(f"🔑 row_key: {row_key}")

    # Crear tabla CON los datos desde el inicio
    table = ui.table(
        columns=columnas,
        rows=rows,  # 👈 CRÍTICO: Pasar datos al crear
        row_key=row_key
    ).classes('w-full h-[300px]')

    # Contador
    ui.label(f"✅ Mostrando {len(rows)} registros")

    return table