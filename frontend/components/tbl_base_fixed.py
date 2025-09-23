
# frontend/components/tbl_base_fixed.py - AGREGAR EXPORTAR Y ACCIONES

from nicegui import ui
import pandas as pd
import io
from typing import Optional, Dict, Any, List
from datetime import datetime

def crear_tabla_fixed(
    nombre: str,
    columnas: list,
    data: pd.DataFrame,
    row_key: str = "id",
    formatos_especiales: Optional[Dict[str, Any]] = None,
    filtros: Optional[List[Dict]] = None,
    relacion_filtros: Optional[Dict[str, str]] = None,
    exportar: bool = False,  # 👈 NUEVO: Botón exportar
    acciones: Optional[list] = None  # 👈 NUEVO: Acciones por fila
):
    """Versión FIXED - Con exportar y acciones"""
    df = data.copy()

    # 1. TÍTULO Y EXPORTAR (NUEVO)
    with ui.row().classes("w-full items-center justify-between mb-4"):
        if nombre:
            ui.label(nombre).classes("text-2xl font-bold text-gray-800")

        if exportar:
            def exportar_excel():
                df_f = df.copy()  # Exportar datos completos (sin filtrar por simplicidad)
                output = io.BytesIO()
                df_f.to_excel(output, index=False)
                filename = f"{nombre}_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
                ui.download(output.getvalue(), filename=filename)

            ui.button("Exportar a Excel", icon="download", on_click=exportar_excel) \
                .classes("export-btn-pro")

    # 2. FILTROS (mantener igual)
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

    # 3. RELACIÓN PADRE-HIJO (mantener igual)
    if relacion_filtros and filter_elements:
        for hijo, padre in relacion_filtros.items():
            if hijo in filter_elements and padre in filter_elements:
                def _update_child_options(_h=hijo, _p=padre):
                    pv = filter_elements[_p].value
                    if pv == "Todos":
                        opts = ["Todos"] + sorted(df[_h].dropna().astype(str).unique().tolist())
                    else:
                        opts = ["Todos"] + sorted(
                            df[df[_p].astype(str) == pv][_h].dropna().astype(str).unique().tolist()
                        )
                    filter_elements[_h].options = opts
                    if filter_elements[_h].value not in opts:
                        filter_elements[_h].value = "Todos"
                    update_table()
                filter_elements[padre].on("update:model-value", _update_child_options)

    # 4. AGREGAR COLUMNA ACCIONES SI HAY ACCIONES (NUEVO)
    columnas_finales = columnas.copy()
    if acciones:
        columnas_finales.append(
            {"name": "acciones", "label": "Acciones", "field": "acciones", "align": "center"}
        )

    # 5. Contador
    result_label = ui.label("").classes("text-sm text-gray-600 mb-2")

    # 6. Tabla básica
    with ui.card().classes("w-full border rounded-lg"):
        table = ui.table(
            columns=columnas_finales,  # 👈 Usar columnas_finales
            rows=[],
            row_key=row_key,
        ).props("pagination rows-per-page=25").classes("h-[500px]")

    # 7. SLOT PARA ACCIONES (NUEVO)
    if acciones:
        # Buscar funciones de info y edit
        info_func = next((accion["func"] for accion in acciones if accion["name"] == "info"), None)
        edit_func = next((accion["func"] for accion in acciones if accion["name"] == "edit"), None)
        info_icon = next((accion["icon"] for accion in acciones if accion["name"] == "info"), "info")
        edit_icon = next((accion["icon"] for accion in acciones if accion["name"] == "edit"), "edit")

        # Slot simple para acciones
        acciones_slot = f"""
        <q-td key="acciones" :props="props">
            <div class="row justify-center gap-1">
                <q-btn icon="{info_icon}" @click="() => window.infoAction(props.row)" flat dense class="action-btn"/>
                <q-btn icon="{edit_icon}" @click="() => window.editAction(props.row)" flat dense class="action-btn"/>
            </div>
        </q-td>
        """
        table.add_slot('body-cell-acciones', acciones_slot)

        # Funciones globales (simplificado)
        def info_action(row):
            if info_func:
                info_func(row)

        def edit_action(row):
            if edit_func:
                edit_func(row)

        # Agregar al contexto global (simplificado)
        ui.add_body_html(f"""
        <script>
            window.infoAction = {info_action};
            window.editAction = {edit_action};
        </script>
        """)

    # 8. Actualización
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

        # Agregar campo "acciones" a cada fila si hay acciones
        if acciones:
            for r in rows:
                r["acciones"] = "acciones"

        table.rows = rows
        result_label.text = f"Mostrando {len(rows)} de {len(df)} registros"

    update_table()

    # 9. Conectar filtros
    if filtros:
        for filter_element in filter_elements.values():
            filter_element.on("update:model-value", lambda: update_table())

    return table
