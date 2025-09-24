# DeepSeek Development operative
# core/layout.py

from nicegui import ui
from core.__version__ import __version__, __build__, __app__

import json
from starlette.requests import Request

# ✅ Cargar menú desde la raíz del proyecto
with open('menu.json', 'r', encoding='utf-8') as f:
    MENU_CONFIG = json.load(f)


# ---------------- SIDEBAR DESDE JSON ----------------
def create_sidebar_from_json(current_path: str):
    """Versión alternativa del sidebar, cargada dinámicamente desde menu.json"""
    with ui.left_drawer().classes(
        'bg-gray-100 border-r border-gray-300 w-60 text-sm pt-2 shadow-sm'
    ):
        for group in MENU_CONFIG:
            expanded = any(current_path.startswith(child["path"]) for child in group["children"])
            with ui.expansion(group["label"], value=expanded).classes(
                'text-gray-800 font-semibold text-sm'
            ):
                for item in group["children"]:
                    active = (current_path == item["path"])
                    ui.link(item["label"], item["path"]).classes(
                        'block px-3 py-1.5 rounded-md transition-colors duration-150 '
                        + (
                            'bg-blue-600 text-white font-bold shadow-sm'
                            if active
                            else 'text-gray-700 hover:bg-blue-50 hover:text-blue-700'
                        )
                    )


# ---------------- HEADER ----------------
def create_header() -> None:
    """Header fijo superior de lado a lado"""
    with ui.header().classes(
        'bg-blue-800 text-white h-12 shadow-md flex items-center px-4'
    ):
        # Botón que SIEMPRE funciona para toggle
        # menu_btn = ui.button(icon='menu', on_click=lambda: ui.left_drawer().toggle()) \
        #     .props('flat round color=white dense')

        ui.label('HIDROBART COSTEO').classes('text-base font-bold tracking-wide')

        ui.button('Perfil', icon='account_circle') \
            .props('flat color=white dense no-caps')


# ---------------- SIDEBAR (HARD-CODEADO) ----------------
def create_sidebar() -> None:
    # 👇 drawer normal, el modo mini se controla con CSS
    with ui.left_drawer(top_corner=True).classes('bg-gray-50 w-60 border-r border-gray-200 pt-16') as drawer:
        drawer.props('mini-to-overlay')

        # 👇 Header del sidebar con toggle
        with ui.row().classes('w-full items-center justify-between px-3 py-2 sidebar-header border-b border-gray-200'):
            ui.label('Navegación').classes('text-sm font-semibold text-gray-700 mini-hidden')
            ui.button(icon='chevron_left', on_click=lambda: drawer.toggle()) \
                .props('flat dense round size=sm') \
                .classes('sidebar-toggle-btn text-gray-500')

        def nav_btn(label: str, icon: str, route: str):
            return ui.button(label, icon=icon, on_click=lambda: ui.navigate.to(route)) \
                .props('flat full-width align=left dense') \
                .classes('justify-start text-sm text-gray-700 hover:text-blue-700 mini-hidden')

        # ---------------- Proveedor ----------------
        with ui.expansion('Proveedores', icon='inventory_2', value=True).classes('w-full text-sm mt-2'):
            nav_btn('Proveedores Activos', 'table_chart', '/v_tblprov_data')
            nav_btn('Proveedores Activos Update', 'table_chart', '/v_tblprov_data_final')
            nav_btn('Proveedores (Todos)', 'fact_check', '/v_tblprov_all')
            nav_btn('Importar Datos', 'upload_file', '/importar_proveedores')

        # ---------------- Productos ----------------
        ui.label('Productos').classes('section-label px-3 pt-3 pb-1 mini-hidden')
        with ui.expansion('Productos', icon='inventory', value=False).classes('w-full text-sm'):
            nav_btn('Listado de Productos', 'list', '/productos/listado')
            nav_btn('Importar Productos', 'file_upload', '/productos/importar')
            nav_btn('Precios de Proveedores', 'price_check', '/productos/precios-proveedor')
            nav_btn('Carga Precios Nuevos', 'system_update_alt', '/productos/carga-precios')
            nav_btn('Cálculo de Costeo', 'calculate', '/productos/costo-destino')
            nav_btn('Lista de Precios', 'request_quote', '/productos/lista-precios')

        # ---------------- Kit Productos ----------------
        ui.label('Kit Productos').classes('section-label px-3 pt-3 pb-1 mini-hidden')
        with ui.expansion('Kit Productos', icon='widgets', value=False).classes('w-full text-sm'):
            nav_btn('Listado de Productos', 'view_list', '/kit/listado')
            nav_btn('Armado de Kit', 'extension', '/kit/armado')
            nav_btn('Costeo', 'calculate', '/kit/costeo')

        # ---------------- Simulación ----------------
        ui.label('Simulación').classes('section-label px-3 pt-3 pb-1 mini-hidden')
        with ui.expansion('Simulación', icon='science', value=False).classes('w-full text-sm'):
            nav_btn('Clientes Especiales', 'star', '/sim/clientes-especiales')
            nav_btn('Campaña', 'campaign', '/sim/campana')
            nav_btn('Mejores Productos', 'trending_up', '/sim/mejores-productos')
            nav_btn('Mejores Márgenes', 'savings', '/sim/mejores-margenes')

        # ---------------- Análisis ----------------
        ui.label('Análisis').classes('section-label px-3 pt-3 pb-1 mini-hidden')
        with ui.column().classes('w-full p-1 gap-1'):
            nav_btn('Reportes', 'analytics', '/reportes')
            nav_btn('Gráficos', 'bar_chart', '/graficos')

        # ---------------- Ejemplos ----------------
        ui.label('Ejemplos').classes('section-label px-3 pt-3 pb-1 mini-hidden')
        with ui.column().classes('w-full p-1 gap-1'):
            nav_btn('Tabla TTBL', 'table_chart', '/ttbl')
            nav_btn('Tabla TTBL2', 'table_chart', '/ttbl2')
            nav_btn('Tabla Pipeline', 'table_chart', '/pipeline')
            nav_btn('Tabla Minimal', 'table_chart', '/test_minimal')

        # ---------------- Sistema ----------------
        ui.label('Sistema').classes('section-label px-3 pt-3 pb-1 mini-hidden')
        with ui.column().classes('w-full p-1 gap-1 border-t'):
            nav_btn('Configuración', 'settings', '/configuracion')
            nav_btn('Ayuda', 'help', '/ayuda')
            nav_btn('Documentación', 'menu_book', '/docs')


# ---------------- FOOTER ----------------
def create_footer() -> None:
    with ui.footer().classes('bg-gray-800 text-white text-center p-2 h-9'):
        ui.label(f'© Hidrobart 2025 | {__app__} v.{__version__} (Build {__build__})').classes('text-xs')


# ---------------- LAYOUT ----------------
def render(content=None) -> None:
    create_header()
    create_sidebar()  # ← usa el hardcodeado
    create_footer()

    # 👇 Contenedor principal con padding superior
    with ui.column().classes('w-full min-h-screen bg-gray-50 pt-16 pl-64 transition-all duration-300'):
        if content:
            content()
