from nicegui import ui
from core import layout
from frontend.components.tbl_base import crear_tabla
import pandas as pd
from core.__version__ import __version__, __build__


@ui.page('/ttbl2')
def ttbl2_page():
    def content():
        with ui.column().classes('w-full p-6'):
            ui.label('Tabla TTBL2 (Demo)').classes('text-2xl font-bold text-gray-800 mb-6')

            # ==== Datos de prueba ====
            data = pd.DataFrame([
                {"id": 1, "proveedor": "Proveedor A", "familia": "Químicos", "code_sys": "Q-001", "nombre": "Producto X", "valor": 1200},
                {"id": 2, "proveedor": "Proveedor B", "familia": "Equipos", "code_sys": "E-010", "nombre": "Producto Y", "valor": 5400},
                {"id": 3, "proveedor": "Proveedor A", "familia": "Químicos", "code_sys": "Q-002", "nombre": "Producto Z", "valor": 3100},
            ])

            # ==== Definir columnas ====
            columnas = [
                {"name": "proveedor", "label": "Proveedor", "field": "proveedor"},
                {"name": "familia", "label": "Familia", "field": "familia"},
                {"name": "code_sys", "label": "Código", "field": "code_sys"},
                {"name": "nombre", "label": "Nombre", "field": "nombre"},
                {"name": "valor", "label": "Valor", "field": "valor"},
            ]

            # ==== Llamada a crear_tabla (sin acciones, sin exportar, con filtros básicos) ====
            crear_tabla(
                nombre="Catálogo de Productos",
                columnas=columnas,
                data=data,
                acciones=None,
                filtros=True,
                exportar=False,
                congelar=None,
            )

    layout.render(content)
