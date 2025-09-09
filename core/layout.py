# Hidrobart Costeo
# Build : 101
# Version 1.0.101.0
# core/layout.py


from nicegui import ui

def render(content: str):
    with ui.header():
        ui.label("AIHB-Costeo - Header")
    with ui.column():
        ui.label(content)
    with ui.footer():
        ui.label("© Hidrobart 2025")
