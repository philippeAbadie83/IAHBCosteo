# frontend/components/tbl_base.py
from typing import Optional, Any, cast
from nicegui import ui
import pandas as pd
import io
from utils.styles import apply_table_styles

def crear_tabla(
    nombre: str,
    columnas: list,
    data: pd.DataFrame,
    acciones: Optional[list] = None,
    filtros: bool = True,
    exportar: bool = False,
    congelar: Optional[list] = None,
):
    """
    Crear tabla universal en NiceGUI con diseño profesional corporativo

    Parámetros:
    - nombre: título visible arriba de la tabla
    - columnas: definición [{name, label, field, sortable}]
    - data: DataFrame de pandas con datos
    - acciones: lista opcional [{'icon': 'edit', 'func': funcion}]
    - filtros: si True agrega buscadores (proveedor, familia, código)
    - exportar: si True agrega botón Exportar a Excel
    - congelar: lista de nombres de columnas a congelar
    """

    # Aplicar estilos de tabla mejorados
    apply_table_styles()

    # ======== Título ========
    if nombre:
        ui.label(nombre).classes("text-xl font-bold mb-4 text-gray-800")

    df = data.copy()

    # ======== Filtros con diseño mejorado ========
    filtro_proveedor = None
    filtro_familia = None
    filtro_codigo = None

    if filtros and not df.empty:
        with ui.row().classes("pro-filter w-full mb-4 gap-4"):
            filtro_proveedor = ui.select(
                options=["Todos"] + sorted(df["proveedor"].unique().tolist()),
                value="Todos",
                label="Proveedor",
            ).classes("w-full md:w-48")

            filtro_familia = ui.select(
                options=["Todos"] + sorted(df["familia"].unique().tolist()),
                value="Todos",
                label="Familia",
            ).classes("w-full md:w-48")

            filtro_codigo = ui.input(
                label="Buscar Código Sys.",
                placeholder="Ingrese código..."
            ).classes("w-full md:w-64")

    # ======== Tabla ========
    if acciones:
        columnas.append(
            {"name": "acciones", "label": "Acciones", "field": "acciones"}
        )

    # Hacer todas las columnas sortable si no está definido
    for col in columnas:
        if 'sortable' not in col:
            col['sortable'] = True

    # Crear contenedor para la tabla con diseño profesional
    with ui.card().classes("pro-table-container w-full no-shadow no-border"):
        table = ui.table(
            columns=columnas,
            rows=[],
        ).props("pagination rows-per-page=20 flat").classes("pro-table")

    # ======== Función de filtrado ========
    def get_filtered_data():
        df_f = df.copy()
        if filtros:
            if filtro_proveedor and filtro_proveedor.value != "Todos":
                df_f = df_f[df_f["proveedor"] == filtro_proveedor.value]
            if filtro_familia and filtro_familia.value != "Todos":
                df_f = df_f[df_f["familia"] == filtro_familia.value]
            if filtro_codigo and filtro_codigo.value:
                # Buscar en code_sys o en la primera columna disponible
                if 'code_sys' in df_f.columns:
                    df_f = df_f[
                        df_f["code_sys"].astype(str).str.contains(
                            filtro_codigo.value, case=False, na=False
                        )
                    ]
                elif 'proveedor' in df_f.columns:
                    df_f = df_f[
                        df_f["proveedor"].astype(str).str.contains(
                            filtro_codigo.value, case=False, na=False
                        )
                    ]
        return df_f

    def format_percentage_value(value):
        """Formatea valores porcentuales con colores y badges según su valor"""
        try:
            num_value = float(value)
            if num_value > 15:
                return f'<span class="alert-badge">{value}%</span>'
            elif num_value > 5:
                return f'<span class="value-badge">{value}%</span>'
            else:
                return f'{value}%'
        except (ValueError, TypeError):
            return str(value)

    # ======== Actualización ========
    def update_table():
        rows = get_filtered_data().to_dict(orient="records")

        # Aplicar formato a los valores porcentuales
        percentage_columns = ['flete_origen', 'arancel', 'gtos_aduana', 'flete_mex', 'total_gastos']
        for row in rows:
            for col in percentage_columns:
                if col in row:
                    row[col] = format_percentage_value(row[col])

        if acciones:
            for r in rows:
                r["acciones"] = r["proveedor"]
        table.rows = rows

        # Mostrar contador de resultados
        if hasattr(update_table, 'result_count'):
            update_table.result_count.text = f"Mostrando {len(rows)} de {len(df)} registros"
        else:
            with ui.row().classes("w-full justify-end mt-2"):
                update_table.result_count = ui.label(f"Mostrando {len(rows)} de {len(df)} registros") \
                    .classes("result-counter-pro")

        # Mostrar contador de resultados con estilo mejorado
        if hasattr(update_table, 'result_count'):
            update_table.result_count.text = f"Mostrando {len(rows)} de {len(df)} registros"
        else:
            with ui.row().classes("w-full justify-end mt-2"):
                update_table.result_count = ui.label(f"Mostrando {len(rows)} de {len(df)} registros") \
                    .classes("result-counter-pro")

    # Configurar eventos de filtrado
    if filtros:
        if filtro_proveedor:
            filtro_proveedor.on("update:model-value", update_table)
        if filtro_familia:
            filtro_familia.on("update:model-value", update_table)
        if filtro_codigo:
            filtro_codigo.on("update:model-value", update_table)

    update_table()

    # ======== Exportar Excel ========
    if exportar:
        def exportar_excel():
            df_f = get_filtered_data()
            output = io.BytesIO()
            df_f.to_excel(output, index=False)
            from datetime import datetime
            filename = f"{nombre}_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
            ui.download(output.getvalue(), filename=filename)

        ui.button("Exportar a Excel", icon="download", on_click=exportar_excel) \
            .classes("export-btn-pro mb-4")

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