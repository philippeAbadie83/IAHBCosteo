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

        # 2. Columnas básicas (sin acciones, sin filtros)
        columnas = [
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True},
            {"name": "familia", "label": "Familia", "field": "familia", "sortable": True},
            {"name": "valor", "label": "Valor", "field": "valor", "sortable": True, "align": "right"},
            {"name": "flete_origen", "label": "Flete Origen %", "field": "flete_origen", "align": "right"},
            {"name": "arancel", "label": "Arancel %", "field": "arancel", "align": "right"},
        ]

        # 3. Tabla FIXED (sin características avanzadas)
        crear_tabla_fixed(
            nombre="Proveedores Activos (FIXED)",
            columnas=columnas,
            data=df,
            row_key="id"
        )

    layout.render(content)