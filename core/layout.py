# DeepSeek y ChatGPT5
# frontend/components/tables.py

from core.__version__ import __version__, __build__, __app__
from nicegui import ui
from typing import Callable, Optional, Any

def create_header() -> None:
    """Crea el header de la aplicación Hidrobart Costeo"""
    with ui.header().classes('bg-blue-800 text-white shadow-lg h-16'):
        with ui.row().classes('w-full items-center justify-between px-6'):
            with ui.row().classes('items-center gap-4'):
                ui.icon('calculate', size='1.8rem', color='white')
                ui.label('AIHB-Costeo').classes('text-2xl font-bold')

            with ui.row().classes('items-center gap-3'):
                ui.button('Dashboard', icon='dashboard').props('flat color=white')
                ui.button('Proyectos', icon='assignment').props('flat color=white')
                ui.button('Costos', icon='paid').props('flat color=white')
                ui.button('Reportes', icon='analytics').props('flat color=white')
                ui.button('Configuración', icon='settings').props('flat color=white')

def create_sidebar() -> None:
    """Crea la barra lateral de navegación para Hidrobart Costeo"""
    with ui.left_drawer().classes('bg-gray-100 w-64 border-r-2 border-gray-200'):
        # Logo y nombre de la app
        with ui.column().classes('w-full items-center p-4 border-b bg-blue-700 text-white'):
            ui.icon('water_damage', size='2.5rem', color='white')
            ui.label('Hidrobart').classes('text-xl font-bold')
            ui.label('Sistema de Costeo').classes('text-sm opacity-90')

        # Navegación principal
        ui.label('Navegación Principal').classes('text-sm font-semibold text-gray-600 px-4 pt-4 pb-2')

        with ui.column().classes('w-full p-2 gap-1'):
            ui.button('Dashboard', icon='dashboard', color='primary').props('flat full-width align=left').classes('justify-start')
            ui.button('Proyectos', icon='assignment', color='primary').props('flat full-width align=left').classes('justify-start')
            ui.button('Costos Directos', icon='construction', color='primary').props('flat full-width align=left').classes('justify-start')
            ui.button('Mano de Obra', icon='engineering', color='primary').props('flat full-width align=left').classes('justify-start')
            ui.button('Materiales', icon='inventory', color='primary').props('flat full-width align=left').classes('justify-start')
            ui.button('Equipos', icon='precision_manufacturing', color='primary').props('flat full-width align=left').classes('justify-start')

        # Análisis y Reportes
        ui.label('Análisis').classes('text-sm font-semibold text-gray-600 px-4 pt-4 pb-2')

        with ui.column().classes('w-full p-2 gap-1'):
            ui.button('Costeo Total', icon='calculate', color='secondary').props('flat full-width align=left').classes('justify-start')
            ui.button('Presupuestos', icon='receipt', color='secondary').props('flat full-width align=left').classes('justify-start')
            ui.button('Reportes', icon='analytics', color='secondary').props('flat full-width align=left').classes('justify-start')
            ui.button('Gráficos', icon='bar_chart', color='secondary').props('flat full-width align=left').classes('justify-start')

        # Configuración y Soporte
        ui.label('Sistema').classes('text-sm font-semibold text-gray-600 px-4 pt-4 pb-2')

        with ui.column().classes('w-full p-2 gap-1 border-t'):
            ui.button('Configuración', icon='settings', color='gray').props('flat full-width align=left').classes('justify-start')
            ui.button('Ayuda', icon='help', color='gray').props('flat full-width align=left').classes('justify-start')
            ui.button('Documentación', icon='menu_book', color='gray').props('flat full-width align=left').classes('justify-start')

def create_footer() -> None:
    """Crea el footer de la aplicación"""
    with ui.footer().classes('bg-gray-800 text-white text-center p-3'):
        ui.label(f'© Hidrobart 2025 | {__app__} v.{__version__} (Build {__build__})').classes('text-sm')

def setup_layout() -> None:
    """Configura el layout completo de la aplicación"""
    create_header()
    create_sidebar()
    create_footer()

def render(content: Optional[Callable[[], None]] = None) -> None:
    """
    Renderiza el layout completo con contenido personalizado

    Args:
        content: Función que renderiza el contenido principal (opcional)
    """
    setup_layout()

    # Área de contenido principal (compensando el sidebar)
    with ui.column().classes('w-full min-h-screen bg-gray-50 ml-64 pt-16'):
        if content:
            content()
        else:
            # Contenido por defecto si no se proporciona
            with ui.column().classes('w-full p-8 items-center justify-center'):
                ui.icon('dashboard', size='4rem', color='gray-400').classes('mb-4')
                ui.label('Bienvenido a Hidrobart Costeo').classes('text-2xl font-semibold text-gray-600 mb-2')
                ui.label('Selecciona una opción del menú para comenzar').classes('text-gray-500')

# Función de ejemplo para mostrar cómo usar el layout
def example_content():
    """Ejemplo de contenido para el layout"""
    with ui.column().classes('w-full p-6'):
        ui.label('Dashboard de Costeo').classes('text-2xl font-bold text-gray-800 mb-6')

        # Tarjetas de resumen
        with ui.row().classes('w-full gap-4 mb-6'):
            with ui.card().classes('p-4 w-48 bg-blue-500 text-white'):
                ui.label('Total Proyectos').classes('text-sm')
                ui.label('24').classes('text-2xl font-bold')

            with ui.card().classes('p-4 w-48 bg-green-500 text-white'):
                ui.label('Costeo Activo').classes('text-sm')
                ui.label('€ 1.2M').classes('text-2xl font-bold')

            with ui.card().classes('p-4 w-48 bg-orange-500 text-white'):
                ui.label('Pendientes').classes('text-sm')
                ui.label('8').classes('text-2xl font-bold')

        # Sección principal
        with ui.card().classes('w-full p-6'):
            ui.label('Proyectos Recientes').classes('text-xl font-semibold mb-4')
            ui.label('Aquí iría la tabla de proyectos...').classes('text-gray-500')

# Versión original de render para compatibilidad (si la necesitas)
def render_old(content: str) -> None:
    """Versión original para compatibilidad con código existente"""
    def render_content():
        with ui.column().classes('w-full p-6'):
            ui.label(content).classes('text-lg')

    render(render_content)

