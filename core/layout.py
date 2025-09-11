# Hidrobart Costeo
# core/layout.py

from core.__version__ import __version__, __build__
print(f"Versión: {__version__}, Build: {__build__}")

from nicegui import ui

def render(content: str):
    with ui.header():
        ui.label("AIHB-Costeo - Header")
    with ui.column():
        ui.label(content)
    with ui.footer():
        ui.label("© Hidrobart 2025 | v.{__version__} (Build {__build__})")
