from nicegui import ui
import pandas as pd
from frontend.components.tbl_base import crear_tabla
from services.db_services import get_proveedores_activos
from utils.helpers import sanitize_dataframe
from core import layout
from core.__version__ import __version__, __build__


@ui.page("/v_tblprov_data")
def v_tblprov_data():
    print(f"[v_tblprov_data] Versión: {__version__}, Build: {__build__}")

    def content():
        # ======== Obtener y sanitizar datos de la BD ========
        df: pd.DataFrame = get_proveedores_activos()
        df = sanitize_dataframe(df)

        # ======== Definir columnas ========
        columnas = [
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True, "align": "left"},
            {"name": "familia", "label": "Familia", "field": "familia", "sortable": True, "align": "left"},
            {"name": "valor", "label": "Valor", "field": "valor", "align": "right"},
            {"name": "flete_origen", "label": "Flete Origen %", "field": "flete_origen", "align": "right"},
            {"name": "arancel", "label": "Arancel %", "field": "arancel", "align": "right"},
            {"name": "gtos_aduana", "label": "Gtos Aduana %", "field": "gtos_aduana", "align": "right"},
            {"name": "flete_mex", "label": "Flete Mex %", "field": "flete_mex", "align": "right"},
            {"name": "total_gastos", "label": "Total Gastos %", "field": "total_gastos", "align": "right"},
            {"name": "comentarios", "label": "Comentarios", "field": "comentarios", "align": "left"},
        ]

        # ======== Crear filtros dinámicos ========
        proveedores = ["Todos"] + sorted(df["proveedor"].dropna().unique().tolist())
        familias = ["Todos"] + sorted(df["familia"].dropna().unique().tolist())

        filter_elements = {}
        with ui.row():
            filter_elements["proveedor"] = ui.select(
                proveedores,
                value="Todos",
                label="Proveedor",
            )
            filter_elements["familia"] = ui.select(
                familias,
                value="Todos",
                label="Familia",
            )

        # Relación padre-hijo: cuando cambia proveedor, actualizar familias
        def update_familias(e):
            prov = e.value
            if prov == "Todos":
                new_familias = ["Todos"] + sorted(df["familia"].dropna().unique().tolist())
            else:
                new_familias = ["Todos"] + sorted(
                    df[df["proveedor"] == prov]["familia"].dropna().unique().tolist()
                )
            filter_elements["familia"].options = new_familias
            filter_elements["familia"].value = "Todos"

        filter_elements["proveedor"].on_value_change(update_familias)

        # ======== Definir formatos especiales ========
        formatos_especiales = {
            "flete_origen": {"tipo": "porcentaje"},
            "arancel": {"tipo": "porcentaje"},
            "gtos_aduana": {"tipo": "porcentaje"},
            "flete_mex": {"tipo": "porcentaje"},
            "total_gastos": {"tipo": "porcentaje"},
        }

        # ======== Funciones de acciones ========
        def mostrar_info(row):
            with ui.dialog() as dialog, ui.card().classes("w-[680px]"):
                ui.label("Detalle del registro").classes("text-lg font-bold mb-2")
                with ui.separator():
                    pass
                with ui.grid(columns=2).classes("gap-2 my-2"):
                    for k, v in row.items():
                        if k == "acciones":
                            continue
                        ui.label(str(k).replace("_", " ").title()).classes("text-sm text-gray-600")
                        ui.label("" if v is None else str(v)).classes("text-sm")
                with ui.row().classes("justify-end mt-2"):
                    ui.button("Cerrar", on_click=dialog.close)
            dialog.open()

        def editar_registro(row):
            ui.notify(f"Editar: {row.get('proveedor', '')}")

        acciones = [
            {"icon": "info", "name": "info", "func": mostrar_info},
            {"icon": "edit", "name": "edit", "func": editar_registro},
        ]

        # ======== Crear tabla genérica ========
        crear_tabla(
            nombre="Proveedores Activos",
            columnas=columnas,
            data=df,
        #    filtros=[
        #        {"type": "select", "column": "proveedor", "label": "Proveedor"},
        #        {"type": "select", "column": "familia", "label": "Familia"},
        #    ],
            exportar=True,
            congelar=["proveedor", "familia"],
            formatos_especiales=formatos_especiales,
            acciones=acciones,
        #    relacion_filtros={"familia": "proveedor"},  # 👈 Jerarquía padre-hijo
        )

    # 👉 Integración al layout
    layout.render(content)
