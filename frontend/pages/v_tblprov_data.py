
# frontend/pages/v_tblprov_data.py

from nicegui import ui
import pandas as pd

from frontend.components.tbl_base import crear_tabla
from services.db_services import get_proveedores_activos, get_catalogo_filtros_prov_famil
from utils.helpers import sanitize_dataframe
from core import layout
from core.__version__ import __version__, __build__


@ui.page("/v_tblprov_data")
def v_tblprov_data():
    print(f"[v_tblprov_data] Versión: {__version__}, Build: {__build__}")

    def content():
        df: pd.DataFrame = get_proveedores_activos()
        df = sanitize_dataframe(df)

        # ======== Catálogo para filtros ========
        #  df_filtros = get_catalogo_filtros_prov_famil()

        # ======== Definir columnas ========
        columnas = [
            {"name": "prov_id", "label": "ID", "field": "prov_id", "sortable": True, "align": "left"},
            {"name": "prov_name", "label": "Proveedor", "field": "prov_name", "sortable": True, "align": "left"},
            {"name": "prov_famil", "label": "Familia", "field": "prov_famil", "sortable": True, "align": "left"},
            {"name": "prov_multip", "label": "Valor", "field": "prov_multip", "align": "right"},
            {"name": "prov_pct_fleteorig", "label": "Flete Origen %", "field": "prov_pct_fleteorig", "align": "right"},
            {"name": "prov_pct_arancel", "label": "Arancel %", "field": "prov_pct_arancel", "align": "right"},
            {"name": "prov_pct_gtoaduana", "label": "Gtos Aduana %", "field": "prov_pct_gtoaduana", "align": "right"},
            {"name": "prov_pct_fletedest", "label": "Flete Mex %", "field": "prov_pct_fletedest", "align": "right"},
            {"name": "prov_pct_totgto", "label": "Total Gastos %", "field": "prov_pct_totgto", "align": "right"},
            {"name": "prov_coment", "label": "Comentarios", "field": "prov_coment", "align": "left"},
        ]


    # ======== Definir filtros ========
     #   filtros = [
     #       {"type": "select", "column": "proveedor", "label": "Proveedor"},
     #       {"type": "select", "column": "familia", "label": "Familia"},
     #   ]
     #   relacion_filtros = {"familia": "proveedor"}  # 👈 relación padre-hijo

    # ======== Formatos especiales ========
        formatos_especiales = {
                "flete_origen": {"tipo": "porcentaje"},
                "arancel": {"tipo": "porcentaje"},
                "gtos_aduana": {"tipo": "porcentaje"},
                "flete_mex": {"tipo": "porcentaje"},
                "total_gastos": {"tipo": "porcentaje"},
            }

        # ======== Acciones ========
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
            exportar=True,
            formatos_especiales=formatos_especiales,
            acciones=acciones,
            )

    # 👉 Integración al layout
    layout.render(content)
