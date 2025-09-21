# frontend/pages/v_tblprov_data.py
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
            {"name": "version", "label": "Versión", "field": "version", "align": "center"},
            {"name": "fecha_update", "label": "Última Actualización", "field": "fecha_update", "align": "center"},
            {"name": "usuario_update", "label": "Actualizado por", "field": "usuario_update", "align": "left"},
        ]

        # ======== Encabezado con botón de exportar ========
        with ui.row().classes("w-full items-center justify-between mb-4"):
            ui.label("Proveedores Activos").classes("text-2xl font-bold text-gray-800")
            ui.button("Exportar Excel", icon="download", on_click=lambda: df.to_excel("Proveedores.xlsx", index=False)) \
                .classes("export-btn-pro")

        # ======== Crear tabla SIN ACCIONES ========
        crear_tabla(
            nombre="",
            columnas=columnas,
            data=df,
            filtros=True,
            exportar=False,   # 🔹 ya lo controlamos arriba
            congelar=["proveedor", "familia"],
        )

    # 👉 Integración al layout
    layout.render(content)