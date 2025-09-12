from nicegui import ui
from frontend.components.tables import AdvancedDataTable
from core import layout

@ui.page('/ttbl3')
def ttbl3_page():
    def content():
        with ui.column().classes('w-full p-6'):
            ui.label('Prueba con AdvancedDataTable').classes('text-2xl font-bold text-gray-800 mb-6')

            # Datos de prueba
            data = [
                {"id": 1, "nombre": "Usuario A", "email": "a@demo.com", "estado": "Activo"},
                {"id": 2, "nombre": "Usuario B", "email": "b@demo.com", "estado": "Inactivo"},
                {"id": 3, "nombre": "Usuario C", "email": "c@demo.com", "estado": "Activo"},
            ]

            columnas = [
                {"name": "id", "label": "ID", "field": "id"},
                {"name": "nombre", "label": "Nombre", "field": "nombre"},
                {"name": "email", "label": "Email", "field": "email"},
                {"name": "estado", "label": "Estado", "field": "estado"},
            ]

            adv_table = AdvancedDataTable()
            adv_table.create_table(
                columns=columnas,
                data=data,
                title="Usuarios Demo"
            )

    layout.render(content)
