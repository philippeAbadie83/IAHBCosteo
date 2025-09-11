# Hidrobart Costeo
# core/layout.py

from core.__version__ import __version__, __build__, __app__
from nicegui import ui

def render(content: str):
    with ui.header():
        ui.label("AIHB-Costeo - Header")
    with ui.column():
        ui.label(content)
    with ui.footer():
        ui.label(f"© Hidrobart 2025 | {__app__} v.{__version__} (Build {__build__})")

