# Hidrobart Costeo
# Build : 101
# Version 1.0.101.0
# app.py

from nicegui import ui
from core import layout

@ui.page('/')
def index_page():
    layout.render("Bienvenido a AIHB-Costeo")

ui.run(title="AIHB-Costeo", reload=False, port=8080)
