# frontend/components/tbl_base
# se usa como framework para todas las tablas del sistemas

from typing import Optional, List, Dict
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
    relacion_filtros: Optional[Dict[str, str]] = None,   # hijo:padre (ej: {"familia": "proveedor"})
):
    """
    Crear tabla universal en NiceGUI completamente GENÉRICA
    con soporte para:
      - Filtros (input, select)
      - Exportar a Excel
      - Acciones por fila
      - Slots especiales (ej. comentarios)
      - Congelar columnas
      - Relación padre-hijo en filtros
    """

    # ======== Estilos ========
    apply_table_styles()
    df = data.copy()

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
    # ACCIONES ESTÁNDAR:
    #   - Info (ℹ️)
    #   - Update (✏️)
    #
    # ACCIONES EXTRA:
    #   - Navegar (🔗)
    #   - Exportar 📑
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
    with ui.card().classes("w-full shadow-md border border-gray-200 rounded-lg"):
        table = ui.table(
            columns=columnas,
            rows=[],
            row_key="id",
        )

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
        comentarios_slot = """
        <q-td key="comentarios" :props="props">
            <div style="max-width:320px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;"
                 :title="props.row.comentarios || ''">
                {{ props.row.comentarios || '' }}
            </div>
        </q-td>
        """
        table.add_slot('body-cell-comentarios', comentarios_slot)

    # ======== Acciones por fila ========
    if acciones:
        info_func = next((accion["func"] for accion in acciones if accion["name"] == "info"), None)
        edit_func = next((accion["func"] for accion in acciones if accion["name"] == "edit"), None)
        info_icon = next((accion["icon"] for accion in acciones if accion["name"] == "info"), "info")
        edit_icon = next((accion["icon"] for accion in acciones if accion["name"] == "edit"), "edit")

        acciones_slot = f"""
        <q-td key="acciones" :props="props">
            <div class="row justify-center gap-1">
                <q-btn icon="{info_icon}" @click="() => $root.infoAction(props.row)" flat dense class="action-btn"/>
                <q-btn icon="{edit_icon}" @click="() => $root.editAction(props.row)" flat dense class="action-btn"/>
            </div>
        </q-td>
        """
        table.add_slot('body-cell-acciones', acciones_slot)

        def add_global_methods():
            def info_action(row):
                if info_func:
                    info_func(row)

            def edit_action(row):
                if edit_func:
                    edit_func(row)

            return {
                'infoAction': info_action,
                'editAction': edit_action
            }

    # ======== Congelar columnas ========
    if congelar:
        for col in congelar:
            table.classes(f"sticky-col sticky-{col}")

    # ======== Relación padre-hijo en filtros ========
    if relacion_filtros and filter_elements:
        for hijo, padre in relacion_filtros.items():
            if hijo in filter_elements and padre in filter_elements:
                def _update_child(e, _h=hijo, _p=padre):
                    pv = filter_elements[_p].value
                    if pv == "Todos":
                        opts = ["Todos"] + sorted(df[_h].dropna().astype(str).unique().tolist())
                    else:
                        opts = ["Todos"] + sorted(
                            df[df[_p].astype(str) == pv][_h].dropna().astype(str).unique().tolist()
                        )
                    filter_elements[_h].options = opts
                    # 👇 aquí está el detalle: en vez de forzar siempre "Todos", conserva valor si sigue válido
                    if filter_elements[_h].value not in opts:
                        filter_elements[_h].value = "Todos"
                    update_table()
                filter_elements[padre].on("update:model-value", _update_child)

    return table
