# core/layout.py
import json
from pathlib import Path
from nicegui import ui
from nicegui import app

from core.__version__ import __version__, __build__, __app__

class NavigationManager:
    def __init__(self, config_path: str = "menu_config.json"):
        self.config_path = Path(config_path)
        self.menu_config = self.load_config()
        self.drawer_collapsed = False

    def load_config(self):
        """Carga la configuración del menú desde JSON"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  No se encontró {self.config_path}")
            # Configuración mínima por defecto con theme
            return {
                "theme": {
                    "primary": "blue",
                    "accent": "red",
                    "style": "corporate"
                },
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

# Instancia global
nav_manager = NavigationManager()

# Función helper para navegación
def make_navigate_handler(path):
    """Crea un handler de navegación para un path específico"""
    def handler():
        app.storage.user['current_path'] = path
        ui.navigate.to(path)
        # Actualizar estados visuales después de navegar
        update_active_states()
    return handler

def toggle_drawer():
    """Toggle entre modo normal y mini del drawer"""
    nav_manager.drawer_collapsed = not nav_manager.drawer_collapsed

    # Cambiar clases CSS del drawer
    ui.run_javascript(f'''
        const drawer = document.querySelector('.q-drawer--left');
        const container = document.querySelector('.q-page-container');

        if (drawer && container) {{
            if ({str(nav_manager.drawer_collapsed).lower()}) {{
                drawer.classList.add('q-drawer--mini');
                container.classList.add('content-collapsed');
            }} else {{
                drawer.classList.remove('q-drawer--mini');
                container.classList.remove('content-collapsed');
            }}
        }}
    ''')

def update_active_states():
    """Actualiza los estados activos de navegación"""
    current_path = app.storage.user.get('current_path')

    # Actualizar usando JavaScript para cambiar clases
    ui.run_javascript(f'''
        // Quitar clase activa de todos los botones
        document.querySelectorAll('.nav-item-active').forEach(btn => {{
            btn.classList.remove('nav-item-active');
        }});

        // Agregar clase activa al botón correspondiente
        const activeBtn = document.querySelector(`[data-path="{current_path}"]`);
        if (activeBtn) {{
            activeBtn.classList.add('nav-item-active');
        }}
    ''')

# ---------------- HEADER ----------------
def create_header(system_menu_config: dict) -> None:
    """Header con botón de toggle mejorado"""
    with ui.header().classes('flex items-center justify-between px-4 text-white shadow-md h-16'):
        # Botón del menú lateral - ahora hace toggle del modo mini
        ui.button(
            icon='menu',
            on_click=toggle_drawer
        ).props('flat round color=white dense').classes('menu-toggle-btn')

        # Título de la aplicación
        ui.label(f'AIHB-Costeo v{__version__}').classes('text-lg font-bold header-title')

        # Menú del sistema
        with ui.row().classes('items-center gap-2'):
            with ui.menu().classes('bg-white shadow-lg') as system_menu:
                for item in system_menu_config.get('children', []):
                    ui.menu_item(
                        item['label'],
                        on_click=make_navigate_handler(item['path'])
                    )

            ui.button(
                system_menu_config['label'],
                icon=system_menu_config['icon'],
                on_click=system_menu.open
            ).props('flat color=white').classes('system-menu-btn')

# ---------------- SIDEBAR CON JSON ----------------
def create_sidebar(menu_sections: list) -> None:
    """Sidebar que se construye dinámicamente desde el JSON"""
    with ui.left_drawer(top_corner=True).classes('bg-grey-2 w-80 border-r border-grey-4 pt-16') as drawer:
        drawer.props('mini-to-overlay')

        # Header del sidebar con botón de colapso
        with ui.row().classes('drawer-header w-full items-center justify-between px-4 py-3 border-b border-grey-4 bg-white'):
            with ui.row().classes('items-center gap-3'):
                ui.icon('navigation', size='md').classes('text-blue-600')
                ui.label('Navegación').classes('section-title text-lg font-bold text-grey-9')

            # Botón de colapso/expand
            ui.button(
                icon='chevron_left',
                on_click=toggle_drawer
            ).props('flat dense round').classes('collapse-btn text-blue-600')

        # Contenido del sidebar desde JSON
        with ui.scroll_area().classes('w-full h-full py-4'):
            with ui.column().classes('w-full px-4 gap-3'):
                for section in menu_sections:
                    create_section_item(section)

def create_section_item(section: dict):
    """Crea un item de sección con sus subitems y estados activos"""

    # Ruta actual
    current_path = app.storage.user.get('current_path')
    # Sección activa si alguno de sus hijos coincide con la ruta actual
    is_section_active = any(child['path'] == current_path for child in section.get('children', []))

    # Encabezado de la sección
    with ui.expansion(
        section['label'],
        icon=section.get('icon', 'folder'),
        value=is_section_active
    ).classes('w-full bg-white rounded-lg shadow-sm'):

        # Subitems de la sección
        with ui.column().classes('w-full pl-4 gap-1'):
            for item in section.get('children', []):
                # Determinar si este item está activo
                is_active = current_path == item['path']

                # Crear botón con data attribute para JavaScript
                button = ui.button(
                    item['label'],
                    icon=item.get('icon', 'chevron_right'),
                    on_click=make_navigate_handler(item['path'])
                ).props('flat dense').classes('nav-item justify-start w-full text-sm hover:bg-blue-1')

                # Agregar data attribute para identificar el botón
                button._props['data-path'] = item['path']

                # Aplicar clase activa si corresponde
                if is_active:
                    button.classes(add='nav-item-active')

                # Agregar texto para modo colapsado
                with button:
                    ui.label(item['label']).classes('nav-item-text')

# ---------------- FOOTER ----------------
def create_footer() -> None:
    with ui.footer().classes('bg-grey-9 text-white text-center p-3'):
        ui.label(f'© Hidrobart 2025 | {__app__} v.{__version__} (Build {__build__})').classes('text-xs')

# ---------------- RENDER ----------------
def render(content=None) -> None:
    """Renderiza el layout completo usando el JSON"""

    menu_config = nav_manager.menu_config

    # Crear componentes
    create_header(menu_config.get('system_menu', {}))
    create_sidebar(menu_config.get('menu_sections', []))
    create_footer()

    with ui.column().classes('w-full min-h-screen pt-16 pl-80'):
        if content:
            content()

# ---------------- OBTENER RUTAS ----------------
def get_menu_routes():
    """Retorna todas las rutas definidas en el menú"""
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