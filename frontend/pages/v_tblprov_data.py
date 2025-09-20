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

        # ======== Definir acciones ========
        def editar_proveedor(proveedor_data):
            """Función para editar un proveedor"""
            ui.notify(f"Editando proveedor: {proveedor_data.get('proveedor', 'N/A')}")
            # Aquí iría la lógica para abrir un diálogo de edición
            print("Datos del proveedor:", proveedor_data)

        def ver_detalles(proveedor_data):
            """Función para ver detalles del proveedor"""
            ui.notify(f"Viendo detalles de: {proveedor_data.get('proveedor', 'N/A')}")
            # Aquí iría la lógica para mostrar detalles
            print("Detalles del proveedor:", proveedor_data)

        acciones = [
            {"icon": "edit", "func": editar_proveedor, "tooltip": "Editar proveedor"},
            {"icon": "visibility", "func": ver_detalles, "tooltip": "Ver detalles"},
        ]

        # ======== Definir columnas ========
        columnas = [
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True},
            {"name": "familia", "label": "Familia", "field": "familia", "sortable": True},
            {"name": "valor", "label": "Valor", "field": "valor", "sortable": True},
            {"name": "flete_origen", "label": "Flete Origen %", "field": "flete_origen", "sortable": True},
            {"name": "arancel", "label": "Arancel %", "field": "arancel", "sortable": True},
            {"name": "gtos_aduana", "label": "Gtos Aduana %", "field": "gtos_aduana", "sortable": True},
            {"name": "flete_mex", "label": "Flete Mex %", "field": "flete_mex", "sortable": True},
            {"name": "total_gastos", "label": "Total Gastos %", "field": "total_gastos", "sortable": True},
            {"name": "comentarios", "label": "Comentarios", "field": "comentarios", "sortable": False},
            {"name": "version", "label": "Versión", "field": "version", "sortable": True},
            {"name": "fecha_update", "label": "Última Actualización", "field": "fecha_update", "sortable": True},
            {"name": "usuario_update", "label": "Actualizado por", "field": "usuario_update", "sortable": True},
        ]

        # ======== Crear tabla ========
        crear_tabla(
            nombre="Proveedores Activos",
            columnas=columnas,
            data=df,
            acciones=acciones,
            filtros=True,
            exportar=True,  # 🔹 Ahora la exportación está integrada en la tabla
            congelar=["proveedor", "familia"],
        )

    # 👉 Integración al layout
    layout.render(content)