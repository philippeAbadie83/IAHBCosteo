# Hidrobart Costeo
# frontend/pages/v_tblprov_data.py

from nicegui import ui
import pandas as pd
from frontend.components.tbl_base import crear_tabla
from services.db_services import get_proveedores_activos  # función que hicimos antes
from core.__version__ import __version__, __build__


@ui.page("/v_tblprov_data")
def v_tblprov_data():
    print(f"[v_tblprov_data] Versión: {__version__}, Build: {__build__}")

    # ======== Obtener datos de la BD ========
    df: pd.DataFrame = get_proveedores_activos()

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

    # ======== Crear tabla ========
    crear_tabla(
        nombre="Proveedores Activos",
        columnas=columnas,
        data=df,
        filtros=True,      # se filtra por proveedor y familia
        exportar=True,     # habilita exportación a Excel
        congelar=["proveedor", "familia"],  # fijar columnas clave
    )
