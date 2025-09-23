# frontend/pages/test_minimal.py

from nicegui import ui
import pandas as pd
from frontend.components.tbl_base_minimal import crear_tabla_minimal
from core import layout

@ui.page("/test_minimal")
def test_minimal():
    def content():
        ui.label("🧪 TEST TABLA MINIMAL").classes("text-2xl font-bold mb-6")

        datos = [
            {"id": 1, "proveedor": "A", "valor": 1.1},
            {"id": 2, "proveedor": "B", "valor": 2.2},
            {"id": 3, "proveedor": "C", "valor": 3.3},
        ]

        df = pd.DataFrame(datos)

        columnas = [
            {"name": "id", "label": "ID", "field": "id", "sortable": True},
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True},
            {"name": "valor", "label": "Valor", "field": "valor", "sortable": True},
        ]

        crear_tabla_minimal(
            nombre="Tabla Minimalista",
            columnas=columnas,
            data=df,
            row_key="id"
        )

    layout.render(content)