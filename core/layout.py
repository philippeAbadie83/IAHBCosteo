# core/layout.py
import json
from pathlib import Path
from nicegui import ui
from core.__version__ import __version__, __build__, __app__

class NavigationManager:
    def __init__(self, config_path: str = "menu_config.json"):
        self.config_path = Path(config_path)
        self.menu_config = self.load_config()

    def load_config(self):
        """Carga la configuración del menú desde JSON"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  No se encontró {self.config_path}")
            # Configuración mínima por defecto
            return {
                "menu_sections": [],
                "system_menu": {
                    "label": "Sistema",
                    "icon": "settings",
                    "children": [
                        {"label": "Configuración", "path": "/configuracion", "icon": "settings"},
                        {"label": "Ayuda", "path": "/ayuda", "icon": "help"}
                    ]
                }
            }

# Función helper para navegación (definida fuera de las funciones)
def make_navigate_handler(path):
    """Crea un handler de navegación para un path específico"""
    def handler():
        ui.navigate.to(path)
    return handler

# ---------------- HEADER ----------------
def create_header(system_menu_config: dict) -> None:
    """Header con menú del sistema"""
    with ui.header().classes(
        'flex items-center justify-between px-4 bg-primary text-white shadow-md h-16'
    ):
        # Botón del menú lateral
        ui.button(icon='menu', on_click=lambda: ui.left_drawer().toggle()) \
            .props('flat round color=white dense')

        # Título de la aplicación
        ui.label(f'AIHB-Costeo v{__version__}').classes('text-lg font-bold')

        # Menú del sistema
        with ui.row().classes('items-center gap-2'):
            with ui.menu().classes('bg-white shadow-lg') as system_menu:
                for item in system_menu_config.get('children', []):
                    # Usar la función helper definida fuera
                    ui.menu_item(
                        item['label'],
                        on_click=make_navigate_handler(item['path'])
                    )

            ui.button(
                system_menu_config['label'],
                icon=system_menu_config['icon'],
                on_click=system_menu.open
            ).props('flat color=white')

# ---------------- SIDEBAR CON JSON ----------------
def create_sidebar(menu_sections: list) -> None:
    """Sidebar que se construye dinámicamente desde el JSON"""
    with ui.left_drawer(top_corner=True).classes('bg-grey-2 w-80 border-r border-grey-4 pt-16') as drawer:
        drawer.props('mini-to-overlay')

        # Header del sidebar
        with ui.row().classes('w-full items-center justify-between px-4 py-3 border-b border-grey-4 bg-white'):
            ui.label('Navegación').classes('text-lg font-bold text-grey-9')
            ui.button(icon='close', on_click=lambda: drawer.toggle()) \
                .props('flat dense round')

        # Contenido del sidebar desde JSON
        with ui.scroll_area().classes('w-full h-full py-4'):
            with ui.column().classes('w-full px-4 gap-3'):
                for section in menu_sections:
                    create_section_item(section)

def create_section_item(section: dict):
    """Crea un item de sección con sus subitems"""

    # Encabezado de la sección
    with ui.expansion(
        section['label'],
        icon=section.get('icon', 'folder'),
        value=False
    ).classes('w-full bg-white rounded-lg shadow-sm'):

        # Subitems de la sección
        with ui.column().classes('w-full pl-4 gap-1'):
            for item in section.get('children', []):
                ui.button(
                    item['label'],
                    icon=item.get('icon', 'chevron_right'),
                    on_click=make_navigate_handler(item['path'])  # Usar la función helper
                ).props('flat dense') \
                 .classes('justify-start w-full text-sm hover:bg-blue-1')

# ---------------- FOOTER ----------------
def create_footer() -> None:
    with ui.footer().classes('bg-grey-9 text-white text-center p-3'):
        ui.label(f'© Hidrobart 2025 | {__app__} v.{__version__} (Build {__build__})').classes('text-xs')

# ---------------- LAYOUT PRINCIPAL ----------------
def render(content=None) -> None:
    """Renderiza el layout completo usando el JSON"""

    # Cargar configuración
    nav_manager = NavigationManager()
    menu_config = nav_manager.menu_config

    # Crear componentes
    create_header(menu_config.get('system_menu', {}))
    create_sidebar(menu_config.get('menu_sections', []))
    create_footer()

    # Contenedor principal
    with ui.column().classes('w-full min-h-screen bg-grey-2 pt-16 pl-80 transition-all duration-300'):
        if content:
            content()

# ---------------- FUNCIÓN PARA OBTENER RUTAS ----------------
def get_menu_routes():
    """Retorna todas las rutas definidas en el menú"""
    nav_manager = NavigationManager()
    menu_config = nav_manager.menu_config

    routes = []

    # Rutas de las secciones principales
    for section in menu_config.get('menu_sections', []):
        for item in section.get('children', []):
            routes.append({
                'path': item['path'],
                'label': item['label'],
                'section': section['label']
            })

    # Rutas del sistema
    system_menu = menu_config.get('system_menu', {})
    for item in system_menu.get('children', []):
        routes.append({
            'path': item['path'],
            'label': item['label'],
            'section': 'Sistema'
        })

    return routes