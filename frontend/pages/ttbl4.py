# frontend/pages/ttbl4.py

from nicegui import ui
from frontend.components.tables import AdvancedDataTable
from core import layout
from data.sample_data import generate_sample_users, get_sample_columns


@ui.page('/ttbl4')
def ttbl4_page():
    def content():
        with ui.column().classes('w-full p-6'):
            ui.label('Usuarios Demo con Sample Data').classes('text-2xl font-bold text-gray-800 mb-6')

            # 🔹 Generar datos y columnas desde sample_data
            data = generate_sample_users(20)
            columnas = get_sample_columns()

            adv_table = AdvancedDataTable()
            adv_table.create_table(
                columns=columnas,
                data=data,
                title="Usuarios de Ejemplo"
            )

    layout.render(content)
