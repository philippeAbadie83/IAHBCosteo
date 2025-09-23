# frontend/components/tbl_base_fixed.py

from nicegui import ui
import pandas as pd
from typing import Optional, Dict, Any  # 👈 Agregar esto


def crear_tabla_fixed(
    nombre: str,
    columnas: list,
    data: pd.DataFrame,
    row_key: str = "id",
    formatos_especiales: Optional[Dict[str, Any]] = None  # 👈 CORREGIDO
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

     # AGREGAR después de update_table():
    if formatos_especiales:
        percent_cols = {c for c, cfg in formatos_especiales.items() if cfg.get('tipo') == 'porcentaje'}
        if percent_cols:
            def _fmt_percent(value):
                try:
                    v = float(str(value).replace('%', '').strip())
                    if 0 <= v <= 1: v = v * 100
                    return f"{int(round(v))}%"
                except: return str(value)

            # Aplicar formato
            for col in percent_cols:
                if col in df.columns:
                    df[col] = df[col].apply(_fmt_percent)
        update_table()  # Re-actualizar




    return table