# app.py

from core.__version__ import __version__, __build__
print(f"Versión: {__version__}, Build: {__build__}")

from nicegui import ui
from core import layout

# 🔹 Importar manualmente las páginas que quieras exponer
import frontend.pages.test_table
import frontend.pages.ttbl
import frontend.pages.ttbl2
import frontend.pages.ttbl3
import frontend.pages.ttbl4
import frontend.pages.ttbl_pipeline
import frontend.pages.v_tblprov_data   # ✅ tu nueva vista

# Configurar estilos globales
def setup_global_styles():
    ui.add_head_html('''
    <style>
    /* Estilos globales para Hidrobart Costeo */
    .bg-gradient-hydro {
        background: linear-gradient(135deg, #0072CE 0%, #00A0E3 100%);
    }
    .cost-card {
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 114, 206, 0.15);
        transition: transform 0.2s ease;
    }
    .cost-card:hover {
        transform: translateY(-2px);
    }
    .currency-cell {
        font-family: 'Courier New', monospace;
        font-weight: 600;
    }
    .q-table th {
        background-color: #f0f8ff !important;
        color: #0072CE !important;
        font-weight: 600;
    }
    .q-table tr:nth-child(even) {
        background-color: #fafafa;
    }
    .q-table tr:hover {
        background-color: #e3f2fd !important;
    }
    </style>
    ''')


@ui.page('/')
def index_page():
    def home_content():
        with ui.column().classes('w-full p-8 items-center justify-center'):
            ui.icon('calculate', size='4rem', color='blue-600').classes('mb-4')
            ui.label('Bienvenido a AIHB-Costeo').classes('text-3xl font-bold text-gray-800 mb-2')
            ui.label('Sistema de Gestión de Costos para Hidrobart').classes('text-lg text-gray-600 mb-6')

            with ui.row().classes('gap-4'):
                # Botones ya existentes
                ui.button('Tabla TTBL', icon='table_chart',
                          on_click=lambda: ui.navigate.to('/ttbl')) \
                    .props('unelevated color=primary')

                ui.button('Tabla TTBL2', icon='table_chart',
                          on_click=lambda: ui.navigate.to('/ttbl2')) \
                    .props('unelevated color=secondary')

                ui.button('Tabla TTBL3', icon='table_chart',
                          on_click=lambda: ui.navigate.to('/ttbl3')).props('unelevated color=secondary')

                ui.button('Tabla TTBL4', icon='table_chart',
                          on_click=lambda: ui.navigate.to('/ttbl4')).props('unelevated color=secondary')

                ui.button('Tabla Pipeline', icon='table_chart',
                          on_click=lambda: ui.navigate.to('/pipeline')).props('unelevated color=secondary')

                # Botón ya existente
                ui.button('Tabla de Prueba', icon='table_chart',
                          on_click=lambda: ui.navigate.to('/tabla-prueba')) \
                    .props('outlined color=secondary')

                ui.button('Ver Proyectos', icon='assignment',
                          on_click=lambda: ui.navigate.to('/proyectos')) \
                    .props('unelevated color=primary')

                # ✅ Nuevo botón para proveedores activos
                ui.button('Proveedores Activos', icon='inventory_2',
                          on_click=lambda: ui.navigate.to('/v_tblprov_data')) \
                    .props('unelevated color=primary')

    layout.render(home_content)


if __name__ in ["__main__", "__mp_main__"]:
    setup_global_styles()
    ui.run(title="AIHB-Costeo", reload=False, port=5858, host="0.0.0.0")
