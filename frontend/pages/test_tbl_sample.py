# frontend/pages/test_tabla_sample.py

from nicegui import ui
import pandas as pd
from frontend.components.tbl_base_simple import crear_tabla_simple
from core import layout

# Datos de sample (los que proporcionaste)
def get_sample_data():
    return pd.DataFrame([
        {"id": 1, "nombre": "Usuario 1", "email": "user1@example.com", "edad": 25, "ciudad": "Madrid"},
        {"id": 2, "nombre": "Usuario 2", "email": "user2@example.com", "edad": 30, "ciudad": "Barcelona"},
        {"id": 3, "nombre": "Usuario 3", "email": "user3@example.com", "edad": 35, "ciudad": "Valencia"},
        {"id": 4, "nombre": "Usuario 4", "email": "user4@example.com", "edad": 28, "ciudad": "Madrid"},
        {"id": 5, "nombre": "Usuario 5", "email": "user5@example.com", "edad": 32, "ciudad": "Sevilla"},
    ])

@ui.page("/test_tabla_sample")
def test_tabla_sample():
    def content():
        ui.label("🧪 TEST CON DATOS SAMPLE").classes("text-3xl font-bold mb-6")

        df = get_sample_data()

        columnas = [
            {"name": "id", "label": "ID", "field": "id", "sortable": True},
            {"name": "nombre", "label": "Nombre", "field": "nombre", "sortable": True},
            {"name": "email", "label": "Email", "field": "email", "sortable": True},
            {"name": "edad", "label": "Edad", "field": "edad", "sortable": True, "align": "center"},
            {"name": "ciudad", "label": "Ciudad", "field": "ciudad", "sortable": True},
        ]

        crear_tabla_simple(
            nombre="Tabla con Datos Sample",
            columnas=columnas,
            data=df,
            row_key="id"
        )

    layout.render(content)