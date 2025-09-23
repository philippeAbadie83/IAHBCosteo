# frontend/pages/v_tblprov_data_fixed.py

from nicegui import ui
import pandas as pd
from frontend.components.tbl_base_fixed import crear_tabla_fixed
from services.db_services import get_proveedores_activos
from utils.helpers import sanitize_dataframe
from core import layout

@ui.page("/v_tblprov_data_fixed")
def v_tblprov_data_fixed():
    def content():
        # 1. Obtener datos
        df: pd.DataFrame = get_proveedores_activos()
        df = sanitize_dataframe(df)

        # 2. Columnas básicas
        columnas = [
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True},
            {"name": "familia", "label": "Familia", "field": "familia", "sortable": True},
            {"name": "valor", "label": "Valor", "field": "valor", "sortable": True, "align": "right"},
            {"name": "flete_origen", "label": "Flete Origen %", "field": "flete_origen", "align": "right"},
            {"name": "arancel", "label": "Arancel %", "field": "arancel", "align": "right"},
            {"name": "gtos_aduana", "label": "Gtos Aduana %", "field": "gtos_aduana", "align": "right"},
            {"name": "flete_mex", "label": "Flete Mex %", "field": "flete_mex", "align": "right"},
            {"name": "total_gastos", "label": "Total Gastos %", "field": "total_gastos", "align": "right"},
        ]

        # 3. Formatos especiales
        formatos_especiales = {
            "flete_origen": {"tipo": "porcentaje"},
            "arancel": {"tipo": "porcentaje"},
            "gtos_aduana": {"tipo": "porcentaje"},
            "flete_mex": {"tipo": "porcentaje"},
            "total_gastos": {"tipo": "porcentaje"},
        }

        # 4. Tabla FIXED con formatos
        crear_tabla_fixed(
            nombre="Proveedores Activos (CON FORMATOS)",
            columnas=columnas,
            data=df,
            row_key="id",
            formatos_especiales=formatos_especiales  # 👈 Paréntesis correctamente cerrado
        )

    layout.render(content)