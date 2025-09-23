# frontend/pages/test_fixed.py

from nicegui import ui
import pandas as pd
from frontend.components.tbl_base_fix import crear_tabla_fix
from core import layout

@ui.page("/test_fix")
def test_fixed():
    def content():
        ui.label("🔧 TEST TABLA FIXED").classes("text-2xl font-bold mb-6")

        # Datos de prueba
        datos = [
            {"id": 1, "proveedor": "ProveedorA", "valor": 1.25},
            {"id": 2, "proveedor": "ProveedorB", "valor": 2.50},
            {"id": 3, "proveedor": "ProveedorC", "valor": 3.75},
            {"id": 4, "proveedor": "ProveedorD", "valor": 4.00},
            {"id": 5, "proveedor": "ProveedorE", "valor": 5.25},
        ]

        df = pd.DataFrame(datos)

        columnas = [
            {"name": "id", "label": "ID", "field": "id", "sortable": True},
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True},
            {"name": "valor", "label": "Valor", "field": "valor", "sortable": True},
        ]

        # Probar la versión fixed
        crear_tabla_fix(
            nombre="Tabla Fixed - Test",
            columnas=columnas,
            data=df,
            row_key="id"
        )

    layout.render(content)