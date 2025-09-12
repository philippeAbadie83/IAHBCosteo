# Hidrobart Costeo
# frontend/components/tbl_base.py

from typing import Optional
from nicegui import ui
import pandas as pd
from typing import cast, Any



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
    Crear tabla universal en NiceGUI

    Parámetros:
    - nombre: título visible arriba de la tabla
    - columnas: definición [{name, label, field, sortable}]
    - data: DataFrame de pandas con datos
    - acciones: lista opcional [{'icon': 'edit', 'func': funcion}]
    - filtros: si True agrega buscadores (proveedor, familia, código)
    - exportar: si True agrega botón Exportar a Excel
    - congelar: lista de nombres de columnas a congelar
    """

    # ======== Título ========
    ui.label(nombre).classes("text-xl font-bold mb-4")

    df = data.copy()

    # ======== Filtros ========
    filtro_proveedor = None
    filtro_familia = None
    filtro_codigo = None

    if filtros and not df.empty:
        with ui.row().classes("gap-4 mb-4"):
            filtro_proveedor = ui.select(
                options=["Todos"] + sorted(df["proveedor"].unique().tolist()),
                value="Todos",
                label="Proveedor",
            )
            filtro_familia = ui.select(
                options=["Todos"] + sorted(df["familia"].unique().tolist()),
                value="Todos",
                label="Familia",
            )
            filtro_codigo = ui.input(label="Buscar Código Sys.")

    # ======== Tabla ========
    if acciones:
        columnas.append(
            {"name": "acciones", "label": "Acciones", "field": "acciones"}
        )

    table = ui.table(
        columns=columnas,
        rows=[],
        row_key="id",
    ).props("pagination-rows='20' dense flat bordered").classes("sticky-header")

    # ======== Función de filtrado ========
    def get_filtered_data():
        df_f = df.copy()
        if filtros:
            if filtro_proveedor and filtro_proveedor.value != "Todos":
                df_f = df_f[df_f["proveedor"] == filtro_proveedor.value]
            if filtro_familia and filtro_familia.value != "Todos":
                df_f = df_f[df_f["familia"] == filtro_familia.value]
            if filtro_codigo and filtro_codigo.value:
                df_f = df_f[
                    df_f["code_sys"].str.contains(
                        filtro_codigo.value, case=False
                    )
                ]
        return df_f

    # ======== Actualización ========
    def update_table():
        rows = get_filtered_data().to_dict(orient="records")
        if acciones:
            for r in rows:
                # solo guardamos el id, no todo el objeto
                r["acciones"] = r["id"]
        table.rows = rows

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
        import io

        def exportar_excel():
            df_f = get_filtered_data()
            output = io.BytesIO()
            df_f.to_excel(output, index=False)
            ui.download(output.getvalue(), filename=f"{nombre}.xlsx")

        ui.button("Exportar a Excel", on_click=exportar_excel)

    # ======== Acciones por fila ========
    if acciones:

        def render_acciones(row):
            with ui.row().classes("gap-1"):
                for accion in acciones:
                    ui.button(
                        icon=accion["icon"],
                        on_click=lambda e, r_id=row["acciones"]: accion["func"](
                            next(
                                x for x in get_filtered_data().to_dict("records")
                                if x["id"] == r_id
                            )
                        ),
                    ).props("flat fab-mini")



        table.add_slot(name="body-cell-acciones", template=cast(Any, render_acciones))



    # ======== Congelar columnas ========
    if congelar:
        for col in congelar:
            table.classes(f"sticky-col sticky-{col}")

    return table
