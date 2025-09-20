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

        # Asegurar que tenemos columna id
        if 'id' not in df.columns:
            df['id'] = df.index + 1

        # ======== Definir columnas ========
        columnas = [
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True},
            {"name": "familia", "label": "Familia", "field": "familia", "sortable": True},
            {"name": "valor", "label": "Valor", "field": "valor"},
            {"name": "flete_origen", "label": "Flete Origen %", "field": "flete_origen"},
            {"name": "arancel", "label": "Arancel %", "field": "arancel"},
            {"name": "gtos_aduana", "label": "Gtos Aduana %", "field": "gtos_aduana"},
            {"name": "flete_mex", "label": "Flete Mex %", "field": "flete_mex"},
            {"name": "total_gastos", "label": "Total Gastos %", "field": "total_gastos"},
            {"name": "comentarios", "label": "Comentarios", "field": "comentarios"},
            {"name": "version", "label": "Versión", "field": "version"},
            {"name": "fecha_update", "label": "Última Actualización", "field": "fecha_update"},
            {"name": "usuario_update", "label": "Actualizado por", "field": "usuario_update"},
        ]

        # ======== Encabezado con botón de exportar ========
        with ui.row().classes("w-full items-center justify-between mb-2"):
            ui.label("Proveedores Activos").classes("text-xl font-bold text-gray-800")
            ui.button("Exportar", icon="download", on_click=lambda: df.to_excel("Proveedores.xlsx", index=False)) \
                .props("outlined dense color=primary") \
                .classes("text-xs px-3 py-1 rounded-md shadow-sm hover:bg-blue-50")

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