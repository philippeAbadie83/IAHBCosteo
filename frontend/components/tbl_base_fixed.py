
# frontend/components/tbl_base_fixed.py - AGREGAR RELACIÓN PADRE-HIJO

from nicegui import ui
import pandas as pd
from typing import Optional, Dict, Any, List


def crear_tabla_fixed(
    nombre: str,
    columnas: list,
    data: pd.DataFrame,
    row_key: str = "id",
    formatos_especiales: Optional[Dict[str, Any]] = None,
    filtros: Optional[List[Dict]] = None,
    relacion_filtros: Optional[Dict[str, str]] = None  # 👈 NUEVO: {"familia": "proveedor"}
):
    """Versión FIXED - Con relación padre-hijo en filtros"""
    df = data.copy()

    # 1. Título simple
    if nombre:
        ui.label(nombre).classes("text-2xl font-bold mb-4")

    # 2. FILTROS
    filter_elements = {}
    if filtros and not df.empty:
        with ui.card().classes("w-full mb-4 p-4 bg-gray-50"):
            ui.label("Filtros").classes("font-bold mb-2")
            with ui.row().classes("w-full items-center gap-4"):
                for filter_config in filtros:
                    filter_type = filter_config.get('type', 'select')
                    filter_label = filter_config.get('label', 'Filtro')
                    filter_column = filter_config.get('column', '')

                    if filter_type == 'select' and filter_column in df.columns:
                        options = ["Todos"] + sorted(df[filter_column].dropna().astype(str).unique().tolist())
                        filter_elements[filter_column] = ui.select(
                            options=options,
                            value="Todos",
                            label=filter_label,
                        ).classes("min-w-[200px]")

    # 3. RELACIÓN PADRE-HIJO (NUEVO)
    if relacion_filtros and filter_elements:
        for hijo, padre in relacion_filtros.items():
            if hijo in filter_elements and padre in filter_elements:
                def _update_child_options(_h=hijo, _p=padre):
                    # Actualizar opciones del filtro hijo basado en padre
                    pv = filter_elements[_p].value
                    if pv == "Todos":
                        opts = ["Todos"] + sorted(df[_h].dropna().astype(str).unique().tolist())
                    else:
                        opts = ["Todos"] + sorted(
                            df[df[_p].astype(str) == pv][_h].dropna().astype(str).unique().tolist()
                        )
                    filter_elements[_h].options = opts
                    # Resetear valor si ya no es válido
                    if filter_elements[_h].value not in opts:
                        filter_elements[_h].value = "Todos"
                    update_table()

                filter_elements[padre].on("update:model-value", _update_child_options)

    # 4. Contador
    result_label = ui.label("").classes("text-sm text-gray-600 mb-2")

    # 5. Tabla básica
    with ui.card().classes("w-full border rounded-lg"):
        table = ui.table(
            columns=columnas,
            rows=[],
            row_key=row_key,
        ).props("pagination rows-per-page=25").classes("h-[500px]")

    # 6. Actualización
    def update_table():
        df_filtrado = df.copy()
        if filtros and filter_elements:
            for filter_config in filtros:
                filter_column = filter_config.get('column', '')
                if filter_column in filter_elements:
                    filter_val = filter_elements[filter_column].value
                    if filter_val != "Todos":
                        df_filtrado = df_filtrado[df_filtrado[filter_column].astype(str) == filter_val]

        rows = df_filtrado.to_dict(orient="records")
        table.rows = rows
        result_label.text = f"Mostrando {len(rows)} de {len(df)} registros"

    update_table()

    # 7. Conectar filtros
    if filtros:
        for filter_element in filter_elements.values():
            filter_element.on("update:model-value", lambda: update_table())

    return table
