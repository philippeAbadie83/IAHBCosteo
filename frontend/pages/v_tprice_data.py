# frontend/pages/v_tprice_data.py

from nicegui import ui
import pandas as pd
from frontend.components.tbl_base_final import crear_tabla_final
from services.db_productos import get_precios
from utils.helpers import sanitize_dataframe
from core import layout

@ui.page("/v_tprice_data")
def v_tprice_data():
    def content():
        # 1. Obtener datos de precios (todos por defecto)
        df: pd.DataFrame = get_precios()

        # 2. Sanitizar (ejemplo: precios con 2 decimales)
        df = sanitize_dataframe(df, decimal_columns=["precio"])

        # 3. Definir columnas de la tabla
        columnas = [
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor"},
            {"name": "familia", "label": "Familia", "field": "familia"},
            {"name": "sku_prov", "label": "SKU Proveedor", "field": "sku_prov"},
            {"name": "precio", "label": "Precio", "field": "precio", "align": "right"},
            {"name": "version", "label": "Versión", "field": "version", "align": "center"},
            {"name": "vigencia_inicio", "label": "Vigencia Inicio", "field": "vigencia_inicio"},
            {"name": "vigencia_fin", "label": "Vigencia Fin", "field": "vigencia_fin"},
            {"name": "fecha_update", "label": "Última Actualización", "field": "fecha_update"},
            {"name": "usuario_update", "label": "Actualizado por", "field": "usuario_update"},
        ]

        # 4. Filtros
        filtros = [
            {"type": "select", "column": "proveedor", "label": "Proveedor"},
            {"type": "select", "column": "familia", "label": "Familia"},
            {"type": "input",  "column": "sku_prov", "label": "SKU Proveedor", "placeholder": "Buscar SKU"},
        ]
        relacion_filtros = {"familia": "proveedor"}

        # 5. Acciones (ejemplo)
        def mostrar_info(row):
            ui.notify(f"Precio {row.get('precio', '')} de {row.get('sku_prov', '')}")

        acciones = [
            {"icon": "info", "name": "info", "func": mostrar_info},
        ]

        # 6. Crear tabla
        crear_tabla_final(
            nombre="Precios Activos",
            columnas=columnas,
            data=df,
            row_key="sku_prov",
            filtros=filtros,
            relacion_filtros=relacion_filtros,
            exportar=True,
            acciones=acciones,
        )

    layout.render(content)
