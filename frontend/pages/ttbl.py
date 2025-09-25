# Hidrobart Costeo
# frontend/pages/ttbl.py

from nicegui import ui
import pandas as pd
from frontend.components.tbl_base import crear_tabla

from core.__version__ import __version__, __build__

@ui.page("/ttbl")
def ttbl():
    print(f"[ttbl] Versión: {__version__}, Build: {__build__}")

    # ======== Datos de prueba ========
    data = pd.DataFrame({
        "id": range(1, 11),
        "proveedor": ["PROV_A"] * 5 + ["PROV_B"] * 5,
        "familia": ["F1", "F2", "F1", "F2", "F3"] * 2,
        "code_sys": [f"C{i:03d}" for i in range(1, 11)],
        "nombre": [f"Producto {i}" for i in range(1, 11)],
        "precio_lista": [100, 200, 150, 120, 300, 110, 220, 330, 440, 550],
    })

    columnas = [
        {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True},
        {"name": "familia", "label": "Familia", "field": "familia", "sortable": True},
        {"name": "code_sys", "label": "Código Sys.", "field": "code_sys", "sortable": True},
        {"name": "nombre", "label": "Producto", "field": "nombre"},
        {"name": "precio_lista", "label": "Precio Lista", "field": "precio_lista", "sortable": True},
    ]

    # ======== Crear tabla sin acciones (para evitar error de serialización) ========
    crear_tabla(
        nombre="Demo Productos",
        columnas=columnas,
        data=data,
        exportar=True,
        congelar=["proveedor", "familia", "code_sys"],
        # acciones=[]  # 🔹 Si lo dejas vacío, tbl_base no dibuja columna de acciones
    )
