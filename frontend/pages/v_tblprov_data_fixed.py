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

        # 2. Sanitizar con todas las mejoras
        df = sanitize_dataframe(df,
            percent_columns=["flete_origen", "arancel", "gtos_aduana", "flete_mex", "total_gastos"],
        )

        # 3. Columnas completas
        columnas = [
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True},
            {"name": "familia", "label": "Familia", "field": "familia", "sortable": True},
            {"name": "valor", "label": "Valor", "field": "valor", "sortable": True, "align": "right"},
            {"name": "flete_origen", "label": "Flete Origen %", "field": "flete_origen", "align": "right"},
            {"name": "arancel", "label": "Arancel %", "field": "arancel", "align": "right"},
            {"name": "gtos_aduana", "label": "Gtos Aduana %", "field": "gtos_aduana", "align": "right"},
            {"name": "flete_mex", "label": "Flete Mex %", "field": "flete_mex", "align": "right"},
            {"name": "total_gastos", "label": "Total Gastos %", "field": "total_gastos", "align": "right"},
            {"name": "comentarios", "label": "Comentarios", "field": "comentarios", "align": "left"},
        ]

        # 4. Filtros
        filtros = [
            {"type": "select", "column": "proveedor", "label": "Proveedor"},
            {"type": "select", "column": "familia", "label": "Familia"},
        ]

        # 5. Relación padre-hijo
        relacion_filtros = {"familia": "proveedor"}

        # 6. Acciones
        def mostrar_info(row):
            ui.notify(f"Info: {row.get('proveedor', '')}")

        def editar_registro(row):
            ui.notify(f"Editar: {row.get('proveedor', '')}")

        acciones = [
            {"icon": "info", "name": "info", "func": mostrar_info},
            {"icon": "edit", "name": "edit", "func": editar_registro},
        ]

        # 7. Crear tabla con todas las funcionalidades
        crear_tabla_fixed(
            nombre="Proveedores Activos (TODAS LAS MEJORAS)",
            columnas=columnas,
            data=df,
            row_key="id",
            filtros=filtros,
            relacion_filtros=relacion_filtros,
            exportar=True,
            acciones=acciones,
        )

    layout.render(content)