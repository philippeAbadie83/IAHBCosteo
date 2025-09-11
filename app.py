# Hidrobart Costeo
# app.py

from core.__version__ import __version__, __build__
print(f"Versión: {__version__}, Build: {__build__}")

from nicegui import ui
from core import layout

@ui.page('/')
def index_page():
    layout.render("Bienvenido a AIHB-Costeo")

ui.run(title="AIHB-Costeo", reload=False, port=8080)
