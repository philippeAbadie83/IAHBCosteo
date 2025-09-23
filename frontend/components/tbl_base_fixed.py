# frontend/components/tbl_base_fixed.py - VERSIÓN MEJORADA

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
    exportar: bool = False,
    acciones: Optional[list] = None,
    truncate_columns: Optional[Dict[str, int]] = None  # 👈 NUEVO: truncamiento
):
    """Versión FIXED mejorada - Con todas las funcionalidades integradas"""
    df = data.copy()

    # 1. TÍTULO Y EXPORTAR - En misma línea con contador
    with ui.row().classes("w-full items-center justify-between mb-2"):  # 👈 menos margin
        if nombre:
            ui.label(nombre).classes("text-2xl font-bold text-gray-800")

        # Contador TEMPORAL aquí
        contador_temp = ui.label("").classes("text-sm text-gray-600")

    # 2. FILTROS Y CONTADOR EN MISMA LÍNEA - Layout compacto
    with ui.row().classes("w-full items-end gap-4 mb-3"):  # 👈 items-end para alinear
        # FILTROS
        filter_elements = {}
        if filtros and not df.empty:
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
                    ).classes("min-w-[180px]")  # 👈 más compacto

        # ESPACIO FLEXIBLE
        ui.space()  # 👈 Empuja el contador a la derecha

        # CONTADOR FIJO A LA DERECHA
        result_label = ui.label("").classes("text-sm text-gray-600 font-medium")

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

    # 4. AGREGAR COLUMNA ACCIONES SI HAY ACCIONES
    columnas_finales = columnas.copy()
    if acciones:
        columnas_finales.append(
            {"name": "acciones", "label": "Acciones", "field": "acciones", "align": "center"}
        )

    # 5. Contador (original - se mantiene por compatibilidad)
    # result_label se usa ahora en la línea de filtros

    # 6. Tabla básica CON MÁS LÍNEAS
    with ui.card().classes("w-full border rounded-lg mt-1"):  # 👈 menos margen arriba
        table = ui.table(
            columns=columnas_finales,
            rows=[],
            row_key=row_key,
        ).props(
            "pagination rows-per-page-options='[25,50,100]' rows-per-page=50"  # 👈 Más líneas
        ).classes("h-[700px]")  # 👈 Más altura

    # 7. SLOT PARA TEXTO TRUNCADO (NUEVO)
    if truncate_columns:
        for col_name, max_len in truncate_columns.items():
            if any(col.get('name') == col_name for col in columnas_finales):
                slot_code = f"""
                <q-td key="{col_name}" :props="props">
                    <div style="max-width: 300px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;"
                         :title="props.row.{col_name} || ''">
                        {{{{ props.row.{col_name} || '' }}}}
                    </div>
                </q-td>
                """
                table.add_slot(f'body-cell-{col_name}', slot_code)

    # 8. SLOT PARA ACCIONES
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

        # Funciones globales
        def info_action(row):
            if info_func:
                info_func(row)

        def edit_action(row):
            if edit_func:
                edit_func(row)

        # Agregar al contexto global
        ui.add_body_html(f"""
        <script>
            window.infoAction = {info_action};
            window.editAction = {edit_action};
        </script>
        """)

    # 9. Actualización
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
        contador_temp.text = ""  # Limpiar temporal

    update_table()

    # 10. Conectar filtros
    if filtros:
        for filter_element in filter_elements.values():
            filter_element.on("update:model-value", lambda: update_table())

    # 11. BOTÓN EXPORTAR (si está activado) - En nueva posición
    if exportar:
        with ui.row().classes("w-full justify-end mt-2"):
            def exportar_excel():
                output = io.BytesIO()
                df.to_excel(output, index=False)  # Exportar datos completos
                filename = f"{nombre}_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
                ui.download(output.getvalue(), filename=filename)

            ui.button("Exportar a Excel", icon="download", on_click=exportar_excel) \
                .classes("export-btn-pro")

    return table