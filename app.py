# app.py

from sys import implementation
from core.__version__ import __version__, __build__
print(f"Versión: {__version__}, Build: {__build__}")

from nicegui import ui
from core.layout import render, get_menu_routes
from utils import styles
from utils.styles import setup_global_styles

# Importar páginas reales
import frontend.pages.v_tprov_data
import frontend.pages.v_tprod_data     # ✅ productos
import frontend.pages.v_tprice_data    # ✅ precios

import frontend.pages.p_imp_prodData   # ✅ Importar página de importar productos
import frontend.pages.p_imp_provData

import frontend.pages.ttbl
import frontend.pages.ttbl2
import frontend.pages.ttbl_pipeline
import frontend.pages.test_tbl_simple
import frontend.pages.test_tbl_sample
import frontend.pages.test_fix
import frontend.pages.test_minimal
import frontend.pages.test_table
import frontend.pages.v_tblprov_data_final

# Importar placeholders (👉 muy importante)
import frontend.pages.placeholders

# Configurar todas las rutas del menú automáticamente
def setup_routes():
    routes = get_menu_routes()
    print("🔍 VERIFICANDO RUTAS DEL JSON:")
    for route in routes:
        # CORRECCIÓN: Usar una función factory para capturar los valores correctamente
        def create_page_handler(route_path, route_label):
            @ui.page(route_path)
            def page_handler():
                def content():
                    with ui.column().classes('w-full p-8'):
                        ui.label(route_label).classes('text-2xl font-bold mb-4')
                        ui.label(f'Ruta: {route_path}').classes('text-gray-600')
                        # Aquí cada página tendrá su contenido específico

                render(content)
            return page_handler

        # Crear y registrar la página
        page_handler = create_page_handler(route['path'], route['label'])
        # La página se registra automáticamente con el decorador @ui.page

# Página principal
@ui.page('/')
def main_page():
    def content():
        with ui.column().classes('w-full p-8'):
            ui.label('Dashboard Principal').classes('text-3xl font-bold mb-8')

            # Mostrar secciones disponibles del menú
            routes = get_menu_routes()
            with ui.grid(columns=3).classes('w-full gap-4'):
                for route in routes:
                    with ui.card().classes('w-full p-4 hover:shadow-lg cursor-pointer'):
                        ui.label(route['label']).classes('font-semibold')
                        ui.label(route['section']).classes('text-sm text-gray-500')
                        ui.label(route['path']).classes('text-xs text-gray-400')

    render(content)

# Configurar rutas
setup_routes()

# Configuración para Azure
if __name__ in ["__main__", "__mp_main__"]:
    styles.setup_global_styles()
    ui.run(
        title=f"AIHB-Costeo v{__version__}",
        reload=True,
        port=5858,
        host="0.0.0.0",
        show=False
    )