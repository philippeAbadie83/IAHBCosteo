# frontend/pages/test_minimal.py

from nicegui import ui
import pandas as pd  # 👈 Agregar este import
from frontend.components.tbl_base_minimal import crear_tabla_minimal
from core import layout

@ui.page("/test_minimal")
def test_minimal():
    def content():
        ui.label("🧪 TEST MÍNIMO SIN ROW_KEY").classes("text-2xl font-bold mb-6")

        datos = [
            {"id": 1, "proveedor": "A", "valor": 1.1},
            {"id": 2, "proveedor": "B", "valor": 2.2},
            {"id": 3, "proveedor": "C", "valor": 3.3},
        ]

        # 👇 CONVERTIR a DataFrame
        df = pd.DataFrame(datos)

        columnas = [
            {"name": "id", "label": "ID", "field": "id"},
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor"},
            {"name": "valor", "label": "Valor", "field": "valor"},
        ]

        crear_tabla_minimal("Tabla Mínima", columnas, df)  # 👈 Pasar DataFrame

    layout.render(content)