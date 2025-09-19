# core/layout.py

from nicegui import ui
from core.__version__ import __version__, __build__, __app__

# ---------------- HEADER ----------------
def create_header() -> None:
    """Header reducido: solo menú lateral y perfil"""
    with ui.header().classes('bg-blue-800 text-white shadow-lg h-14'):
        with ui.row().classes('w-full items-center justify-between px-4'):
            ui.button(icon='menu', on_click=lambda: ui.left_drawer().toggle()) \
                .props('flat round color=white dense')
            ui.button('Perfil', icon='account_circle').props('flat color=white dense')


# ---------------- SIDEBAR ----------------
def create_sidebar() -> None:
    """Menú lateral estilizado"""
    with ui.left_drawer().classes('bg-gray-50 w-60 border-r border-gray-200'):
        # Logo
        with ui.column().classes('w-full items-center p-3 border-b bg-blue-700 text-white'):
            ui.icon('water_damage', size='2rem', color='white')
            ui.label('Hidrobart').classes('text-base font-bold')
            ui.label('Sistema de Costeo').classes('text-xs opacity-80')

        def nav_btn(label: str, icon: str, route: str):
            return ui.button(label, icon=icon, on_click=lambda: ui.navigate.to(route)) \
                .props('flat full-width align=left dense') \
                .classes('justify-start text-sm text-gray-700 hover:text-blue-700')

        # Secciones principales
        ui.label('Navegación Principal').classes('text-xs font-semibold text-gray-500 px-3 pt-3 pb-1')
        with ui.column().classes('w-full p-1 gap-1'):
            nav_btn('Dashboard', 'dashboard', '/')

            # Proveedores
            with ui.expansion('Proveedores', icon='inventory_2', value=True).classes('w-full text-sm'):
                nav_btn('Tabla Proveedores Activos', 'table_chart', '/v_tblprov_data')
                nav_btn('Importar Proveedores', 'upload_file', '/importar_proveedores')

            # Costos
            nav_btn('Costos de Productos', 'inventory', '/costos')
            nav_btn('Cálculos de Costo', 'calculate', '/calculos')
            nav_btn('Lista de Precios', 'request_quote', '/precios')
            nav_btn('Lista de Precios Simulados', 'price_change', '/precios-simulados')

        # Análisis
        ui.label('Análisis').classes('text-xs font-semibold text-gray-500 px-3 pt-3 pb-1')
        with ui.column().classes('w-full p-1 gap-1'):
            nav_btn('Reportes', 'analytics', '/reportes')
            nav_btn('Gráficos', 'bar_chart', '/graficos')

        # Ejemplos
        ui.label('Ejemplos').classes('text-xs font-semibold text-gray-500 px-3 pt-3 pb-1')
        with ui.column().classes('w-full p-1 gap-1'):
            nav_btn('Tabla TTBL', 'table_chart', '/ttbl')
            nav_btn('Tabla TTBL2', 'table_chart', '/ttbl2')
            nav_btn('Tabla Pipeline', 'table_chart', '/pipeline')

        # Sistema
        ui.label('Sistema').classes('text-xs font-semibold text-gray-500 px-3 pt-3 pb-1')
        with ui.column().classes('w-full p-1 gap-1 border-t'):
            nav_btn('Configuración', 'settings', '/configuracion')
            nav_btn('Ayuda', 'help', '/ayuda')
            nav_btn('Documentación', 'menu_book', '/docs')


# ---------------- FOOTER ----------------
def create_footer() -> None:
    with ui.footer().classes('bg-gray-800 text-white text-center p-2 h-9'):
        ui.label(f'© Hidrobart 2025 | {__app__} v.{__version__} (Build {__build__})') \
            .classes('text-xs')


# ---------------- LAYOUT ----------------
def render(content=None) -> None:
    """Renderiza header + sidebar + footer + contenido"""
    create_header()
    create_sidebar()
    create_footer()

    with ui.column().classes('w-full min-h-screen bg-gray-50 ml-60 pt-14'):
        if content:
            content()
