# frontend/components/tbl_base.py
from typing import Optional, Any, cast, List, Dict
from nicegui import ui
import pandas as pd
import io
from utils.styles import apply_table_styles

def crear_tabla(
    nombre: str,
    columnas: list,
    data: pd.DataFrame,
    acciones: Optional[list] = None,
    filtros: Optional[List[Dict]] = None,
    exportar: bool = False,
    congelar: Optional[list] = None,
    formatos_especiales: Optional[Dict] = None,
):
    """
    Crear tabla universal en NiceGUI completamente GENÉRICA
    """
    # Aplicar estilos de tabla mejorados
    apply_table_styles()

    # ======== Título y Botón de Exportar ========
    with ui.row().classes("w-full items-center justify-between mb-4"):
        if nombre:
            ui.label(nombre).classes("text-2xl font-bold text-gray-800")

        if exportar:
            def exportar_excel():
                df_f = get_filtered_data()
                output = io.BytesIO()
                df_f.to_excel(output, index=False)
                from datetime import datetime
                filename = f"{nombre}_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
                ui.download(output.getvalue(), filename=filename)

            ui.button("Exportar a Excel", icon="download", on_click=exportar_excel) \
                .classes("export-btn-pro")

    df = data.copy()

    # ======== Filtros ========
    filter_elements = {}

    if filtros and not df.empty:
        with ui.card().classes("pro-filter w-full mb-4"):
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

                    elif filter_type == 'input':
                        placeholder = filter_config.get('placeholder', 'Buscar...')
                        filter_elements[filter_column] = ui.input(
                            label=filter_label,
                            placeholder=placeholder
                        ).classes("min-w-[250px]")

    # ======== Tabla ========
    if acciones:
        columnas.append(
            {"name": "acciones", "label": "Acciones", "field": "acciones", "align": "center"}
        )

    # Configurar propiedades de columnas
    for col in columnas:
        if 'sortable' not in col:
            col['sortable'] = True
        if 'align' not in col:
            col['align'] = 'left'

    # Crear contenedor para la tabla
    with ui.card().classes("w-full no-shadow no-border"):
        table = ui.table(
            columns=columnas,
            rows=[],
        ).props("pagination rows-per-page=20 flat")

    # ======== Función de filtrado ========
    def get_filtered_data():
        df_f = df.copy()

        if filtros and filter_elements:
            for filter_config in filtros:
                filter_column = filter_config.get('column', '')
                filter_type = filter_config.get('type', 'select')

                if filter_column in filter_elements:
                    filter_element = filter_elements[filter_column]

                    if filter_type == 'select' and filter_element.value != "Todos":
                        df_f = df_f[df_f[filter_column].astype(str) == filter_element.value]

                    elif filter_type == 'input' and filter_element.value:
                        search_text = filter_element.value.lower()
                        df_f = df_f[df_f[filter_column].astype(str).str.lower().str.contains(search_text, na=False)]

        return df_f

    # APPROACH ALTERNATIVO - Modificar los datos para usar tuplas
    def aplicar_formatos_especiales(row):
        if formatos_especiales:
            for col_name, formato_config in formatos_especiales.items():
                if col_name in row and row[col_name] is not None:
                    if formato_config.get('tipo') == 'porcentaje':
                        try:
                            value = row[col_name]
                            if isinstance(value, (int, float)) or (isinstance(value, str) and value.replace('.', '').replace('%', '').isdigit()):
                                num_value = float(str(value).replace('%', ''))

                                # ✅ NiceGUI acepta tuplas (contenido, clase)
                                if num_value > 15:
                                    row[col_name] = (f'{num_value}%', 'alert-badge')
                                elif num_value > 5:
                                    row[col_name] = (f'{num_value}%', 'value-badge')
                                else:
                                    row[col_name] = f'{num_value}%'
                        except (ValueError, TypeError):
                            row[col_name] = str(row[col_name])
        return row



    # ======== Actualización ========
    def update_table():
        df_filtrado = get_filtered_data()
        rows = df_filtrado.to_dict(orient="records")

        # ✅ ELIMINAR la llamada a aplicar_formatos_especiales()
        # Los formatos ahora se manejan via slots

        if acciones:
            for row in rows:
                row["acciones"] = "acciones"

        table.rows = rows

        # Mostrar contador de resultados
        result_text = f"Mostrando {len(rows)} de {len(df)} registros"
        if hasattr(update_table, 'result_count'):
            update_table.result_count.text = result_text
        else:
            with ui.row().classes("w-full justify-end mt-2"):
                update_table.result_count = ui.label(result_text).classes("result-counter-pro")

    # Configurar eventos de filtrado
    if filtros:
        for filter_element in filter_elements.values():
            filter_element.on("update:model-value", lambda: update_table())

    update_table()

    # ======== Acciones por fila ========
    if acciones:
        def render_acciones(row):
            with ui.row().classes("gap-1 justify-center"):
                for accion in acciones:
                    ui.button(
                        icon=accion["icon"],
                        on_click=lambda e, r=row: accion["func"](r),
                    ).props("flat dense").classes("action-btn")

        table.add_slot("body-cell-acciones", cast(Any, render_acciones))

    # ======== Congelar columnas ========
    if congelar:
        for col in congelar:
            table.classes(f"sticky-col sticky-{col}")

    return table