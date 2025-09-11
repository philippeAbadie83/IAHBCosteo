# Hidrobart Costeo
# frontend/pages/index.py

from nicegui import ui
from core.__version__ import __version__, __build__


@ui.page("/")
def index():
    ui.label(f"Hidrobart Costeo - Versión {__version__} (Build {__build__})") \
        .classes("text-2xl font-bold mb-6")

    ui.label("📑 Páginas disponibles").classes("text-lg mb-4")

    with ui.column().classes("gap-2"):
        # Links a las páginas registradas
        ui.link("➡️ Tabla Demo (ttbl)", "/ttbl")

        # conforme agregues más, las listamos aquí:
        # ui.link("➡️ Otra página", "/otra-pagina")
