# core/layout.py

from nicegui import ui
from core.__version__ import __version__, __build__, __app__

# ---------------- HEADER ----------------
def create_header() -> None:
    """Header reducido: solo menú lateral y perfil"""
    with ui.header().classes('bg-blue-800 text-white shadow-lg h-16'):
        with ui.row().classes('w-full items-center justify-between px-6'):
            # Botón para abrir/cerrar el sidebar
            ui.button(icon='menu', on_click=lambda: ui.left_drawer().toggle()) \
                .props('flat round color=white')

            # Solo Perfil a la derecha
            with ui.row().classes('items-center gap-3'):
                ui.button('Perfil', icon='account_circle').props('flat color=white')


# ---------------- SIDEBAR ----------------
def create_sidebar() -> None:
    """Menú lateral reorganizado"""
    with ui.left_drawer().classes('bg-gray-100 w-64 border-r-2 border-gray-200'):
        # Logo
        with ui.column().classes('w-full items-center p-4 border-b bg-blue-700 text-white'):
            ui.icon('water_damage', size='2.5rem', color='white')
            ui.label('Hidrobart').classes('text-xl font-bold')
            ui.label('Sistema de Costeo').classes('text-sm opacity-90')

        # Secciones principales
        ui.label('Navegación Principal').classes('text-sm font-semibold text-gray-600 px-4 pt-4 pb-2')

        with ui.column().classes('w-full p-2 gap-1'):
            # Dashboard
            ui.button('Dashboard', icon='dashboard',
                      on_click=lambda: ui.navigate.to('/')) \
                .props('flat full-width align=left').classes('justify-start')

            # Proveedores (submenú)
            with ui.expansion('Proveedores', icon='inventory_2', value=True).classes('w-full'):
                ui.button('Tabla Proveedores Activos', icon='table_chart',
                          on_click=lambda: ui.navigate.to('/v_tblprov_data')) \
                    .props('flat full-width align=left').classes('justify-start')
                ui.button('Importar Proveedores', icon='upload_file',
                          on_click=lambda: ui.navigate.to('/importar_proveedores')) \
                    .props('flat full-width align=left').classes('justify-start')

            # Costos
            ui.button('Costos de Productos', icon='inventory',
                      on_click=lambda: ui.navigate.to('/costos')) \
                .props('flat full-width align=left').classes('justify-start')
            ui.button('Cálculos de Costo', icon='calculate',
                      on_click=lambda: ui.navigate.to('/calculos')) \
                .props('flat full-width align=left').classes('justify-start')
            ui.button('Lista de Precios', icon='request_quote',
                      on_click=lambda: ui.navigate.to('/precios')) \
                .props('flat full-width align=left').classes('justify-start')
            ui.button('Lista de Precios Simulados', icon='price_change',
                      on_click=lambda: ui.navigate.to('/precios-simulados')) \
                .props('flat full-width align=left').classes('justify-start')

        # Análisis
        ui.label('Análisis').classes('text-sm font-semibold text-gray-600 px-4 pt-4 pb-2')
        with ui.column().classes('w-full p-2 gap-1'):
            ui.button('Reportes', icon='analytics',
                      on_click=lambda: ui.navigate.to('/reportes')) \
                .props('flat full-width align=left').classes('justify-start')
            ui.button('Gráficos', icon='bar_chart',
                      on_click=lambda: ui.navigate.to('/graficos')) \
                .props('flat full-width align=left').classes('justify-start')

        # Sistema
        ui.label('Sistema').classes('text-sm font-semibold text-gray-600 px-4 pt-4 pb-2')
        with ui.column().classes('w-full p-2 gap-1 border-t'):
            ui.button('Configuración', icon='settings',
                      on_click=lambda: ui.navigate.to('/configuracion')) \
                .props('flat full-width align=left').classes('justify-start')
            ui.button('Ayuda', icon='help',
                      on_click=lambda: ui.navigate.to('/ayuda')) \
                .props('flat full-width align=left').classes('justify-start')
            ui.button('Documentación', icon='menu_book',
                      on_click=lambda: ui.navigate.to('/docs')) \
                .props('flat full-width align=left').classes('justify-start')


# ---------------- FOOTER ----------------
def create_footer() -> None:
    """Footer simple"""
    with ui.footer().classes('bg-gray-800 text-white text-center p-3'):
        ui.label(f'© Hidrobart 2025 | {__app__} v.{__version__} (Build {__build__})').classes('text-sm')


# ---------------- LAYOUT ----------------
def render(content=None) -> None:
    """Renderiza header + sidebar + footer + contenido"""
    create_header()
    create_sidebar()
    create_footer()

    with ui.column().classes('w-full min-h-screen bg-gray-50 ml-64 pt-16'):
        if content:
            content()
