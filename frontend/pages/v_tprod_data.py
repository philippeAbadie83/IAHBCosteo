# Frontend/pages/v_tblprod_data.py

from nicegui import ui
import pandas as pd
from frontend.components.tbl_base_final import crear_tabla_final
from services.db_productos import get_productos_activos
from utils.helpers import sanitize_dataframe
from core import layout

@ui.page("/v_tprod_data")
def v_tblprod_data_page():
    def content():
        # 1. Obtener datos
        df: pd.DataFrame = get_productos_activos()

        # 2. Sanitizar (ejemplo: si quieres formatear precios)
        df = sanitize_dataframe(df)

        # 3. Definir columnas
        columnas = [
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "align": "left"},
            {"name": "familia", "label": "Familia", "field": "familia", "align": "left"},
            {"name": "sku_prov", "label": "SKU Proveedor", "field": "sku_prov", "align": "left"},
            {"name": "sku_sys", "label": "SKU Sistema", "field": "sku_sys", "align": "left"},
            {"name": "nombre", "label": "Nombre Producto", "field": "nombre", "align": "left"},
            {"name": "precio_lista", "label": "Precio Lista", "field": "precio_lista", "align": "right"},
            {"name": "version", "label": "Versión", "field": "version", "align": "center"},
            {"name": "fecha_update", "label": "Última Actualización", "field": "fecha_update", "align": "center"},
            {"name": "usuario_update", "label": "Actualizado por", "field": "usuario_update", "align": "left"},
        ]


        # 4. Filtros
        filtros = [
            {"type": "select", "column": "proveedor", "label": "Proveedor"},
            {"type": "select", "column": "familia", "label": "Familia"},
        ]
        relacion_filtros = {"familia": "proveedor"}

        # 5. Acciones
        def mostrar_info(row):
            ui.notify(f"Info: {row.get('nombre', '')}")

        acciones = [
            {"icon": "info", "name": "info", "func": mostrar_info},
        ]

        # 6. Crear tabla
        crear_tabla_final(
            nombre="Productos Activos",
            columnas=columnas,
            data=df,
            row_key="id",
            filtros=filtros,
            relacion_filtros=relacion_filtros,
            exportar=True,
            acciones=acciones,
        )

    layout.render(content)
