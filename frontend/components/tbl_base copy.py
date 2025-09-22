# frontend/components/tbl_base.py
from typing import Optional, Any, cast, List, Dict
from nicegui import ui
import pandas as pd
import io
from utils.styles import apply_table_styles
from typing import Any


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

    # ===============================================================
    # ACCIONES ESTÁNDAR (en esta app):
    #   - Info (ℹ️)   → ver detalles en dialog
    #   - Update (✏️) → editar registro en dialog/formulario
    #
    # ACCIONES EXTRA (opcional, no usadas en esta app):
    #   - Navegar (🔗)
    #   - Seleccionar/Exportar 📑
    #   - Duplicar 📄
    #   - Activar/Desactivar 🔄
    # ===============================================================
    if acciones:
        columnas.append(
            {"name": "acciones", "label": "Acciones", "field": "acciones", "align": "center"}
        )

    # ======== Configurar propiedades de columnas ========
    for col in columnas:
        if 'sortable' not in col:
            col['sortable'] = True
        if 'align' not in col:
            col['align'] = 'left'

    # ======== Crear la tabla ========
    with ui.card().classes("w-full no-shadow no-border"):
        table = ui.table(
            columns=columnas,
            rows=[],
        ).props(
            "pagination rows-per-page-options='10,25,50,75,100' rows-per-page=25 virtual-scroll"
        ).classes("h-[600px]")

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
                        s = filter_element.value.lower()
                        df_f = df_f[df_f[filter_column].astype(str).str.lower().str.contains(s, na=False)]
        return df_f

    # ======== Helpers de formato ========
    def _fmt_percent(value) -> str:
        try:
            v = float(str(value).replace('%', '').strip())
            if 0 <= v <= 1:
                v = v * 100
            return f"{int(round(v))}%"
        except Exception:
            return str(value)

    percent_cols = set()
    if formatos_especiales:
        percent_cols = {c for c, cfg in formatos_especiales.items() if cfg.get('tipo') == 'porcentaje'}

    # ======== Actualización de la tabla ========
    def update_table():
        df_filtrado = get_filtered_data()
        rows = df_filtrado.to_dict(orient="records")

        if percent_cols:
            for r in rows:
                for c in percent_cols:
                    if c in r and r[c] is not None:
                        r[c] = _fmt_percent(r[c])

        if acciones:
            for r in rows:
                r["acciones"] = "acciones"

        table.rows = rows

        result_text = f"Mostrando {len(rows)} de {len(df)} registros"
        if hasattr(update_table, 'result_count'):
            update_table.result_count.text = result_text
        else:
            with ui.row().classes("w-full justify-end mt-2"):
                update_table.result_count = ui.label(result_text).classes("result-counter-pro")

    if filtros:
        for filter_element in filter_elements.values():
            filter_element.on("update:model-value", lambda: update_table())

    update_table()

    # ======== Slot para truncar 'comentarios' ========
    if any(col.get('name') == 'comentarios' for col in columnas):
        def render_comentarios(row):
            val = str(row.get('comentarios', '') or '')
            ui.html(
                f"<div style=\"max-width:320px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;\" "
                f"title=\"{val}\">{val}</div>"
            )
      #  table.add_slot("body-cell-comentarios", cast(Any, render_comentarios))

        table.add_slot("body-cell-comentarios", cast(Any, lambda row: render_comentarios(row)))


    # ======== Acciones por fila ========
    if acciones:

        def _open_info_dialog(r: dict):
            with ui.dialog() as dialog, ui.card().classes("w-[680px]"):
                ui.label("Detalle del registro").classes("text-lg font-bold mb-2")
                with ui.separator():
                    pass
                with ui.grid(columns=2).classes("gap-2 my-2"):
                    for k, v in r.items():
                        if k == 'acciones':
                            continue
                        ui.label(str(k).replace('_', ' ').title()).classes("text-sm text-gray-600")
                        ui.label("" if v is None else str(v)).classes("text-sm")
                with ui.row().classes("justify-end mt-2"):
                    ui.button("Cerrar", on_click=dialog.close)
            dialog.open()

        def render_acciones(row):
            with ui.row().classes("gap-1 justify-center"):
                for accion in acciones:
                    if accion["name"] == "info":
                        ui.button(
                            icon=accion["icon"],
                            on_click=lambda e, r=row, f=accion["func"]: f(r),
                        ).props("flat dense").classes("action-btn")
                    elif accion["name"] == "edit":
                        ui.button(
                            icon=accion["icon"],
                            on_click=lambda e, r=row, f=accion["func"]: f(r),
                        ).props("flat dense").classes("action-btn")

        table.add_slot("body-cell-acciones", cast(Any, lambda row: render_acciones(row)))


    if congelar:
        for col in congelar:
            table.classes(f"sticky-col sticky-{col}")

    return table
