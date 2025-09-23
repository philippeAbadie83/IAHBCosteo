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

        # 2. Definir columnas que son porcentajes
        percent_columns = ["flete_origen", "arancel", "gtos_aduana", "flete_mex", "total_gastos"]

        # 3. Sanitizar INCLUYENDO porcentajes
        df = sanitize_dataframe(df, percent_columns=percent_columns)

        # 4. Columnas básicas
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

        # 5. FILTROS (NUEVO)
        filtros = [
            {"type": "select", "column": "proveedor", "label": "Proveedor"},
            {"type": "select", "column": "familia", "label": "Familia"},
        ]

        # 6. RELACIÓN PADRE-HIJO (NUEVO)
        relacion_filtros = {"familia": "proveedor"}  # 👈 hijo: padre

        # 7. ACCIONES (NUEVO)
        def mostrar_info(row):
            ui.notify(f"Info: {row.get('proveedor', '')}")

        def editar_registro(row):
            ui.notify(f"Editar: {row.get('proveedor', '')}")

        acciones = [
            {"icon": "info", "name": "info", "func": mostrar_info},
            {"icon": "edit", "name": "edit", "func": editar_registro},
        ]

        #*** Tabla FIXED con TODO
        crear_tabla_fixed(
            nombre="Proveedores Activos (CON EXPORTAR Y ACCIONES)",
            columnas=columnas,
            data=df,
            row_key="id",
            filtros=filtros,
            relacion_filtros=relacion_filtros,
            exportar=True,  # 👈 PROBAR EXPORTAR
            acciones=acciones  # 👈 PROBAR ACCIONES
        )


    layout.render(content)