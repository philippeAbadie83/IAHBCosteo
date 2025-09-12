from nicegui import ui
from core import layout
from frontend.components.tbl_base import crear_tabla
import pandas as pd

import pandas as pd

# 🔹 Datos de ejemplo (en producción vendrían de MySQL)
data = [
    {"id": 1, "oportunidad": "Opp1 HEINEKEN", "responsable": "Philippe", "estado": "Pipeline", "monto": 1000, "due": "2025-09-20", "pos_cliente": "Nuevo", "linea": "Ambos", "proceso": "Acercamiento, Cita, Presentación, Cotización"},
    {"id": 2, "oportunidad": "Opp2 KRAFT", "responsable": "Philippe", "estado": "Stand-by", "monto": 750, "due": "2025-09-12", "pos_cliente": "Nuevo", "linea": "HBQ", "proceso": "Acercamiento, Cita, Presentación"},
    {"id": 3, "oportunidad": "Opp3 FENSA", "responsable": "Philippe", "estado": "Descartado", "monto": 3000, "due": "2025-09-18", "pos_cliente": "Recuperado", "linea": "HBL", "proceso": "Acercamiento, Cita"},
    {"id": 4, "oportunidad": "Opp4 Carbotecnia", "responsable": "Philippe", "estado": "Pipeline", "monto": 5000, "due": "2025-09-17", "pos_cliente": "Legacy", "linea": "HBL", "proceso": "Acercamiento, Cita"},
]
pipeline_df = pd.DataFrame(data)


@ui.page('/pipeline')
def pipeline_page():
    def content():
        with ui.column().classes('w-full p-6'):
            ui.label('Pipeline Comercial').classes('text-2xl font-bold mb-6')

            columnas = [
                {'name': 'oportunidad', 'label': 'Oportunidad', 'field': 'oportunidad'},
                {'name': 'responsable', 'label': 'Responsable', 'field': 'responsable'},
                {'name': 'estado', 'label': 'Estado', 'field': 'estado'},
                {'name': 'monto', 'label': 'Monto', 'field': 'monto'},
                {'name': 'due', 'label': 'Due Date', 'field': 'due'},
                {'name': 'pos_cliente', 'label': 'PosCliente', 'field': 'pos_cliente'},
                {'name': 'linea', 'label': 'Línea', 'field': 'linea'},
                {'name': 'proceso', 'label': 'Proceso', 'field': 'proceso'},
            ]

            # Aquí reusar crear_tabla de tbl_base
            crear_tabla(
                nombre="Pipeline",
                columnas=columnas,
                data=pipeline_df,
                filtros=True,
                exportar=False,
                acciones=None
            )

    layout.render(content)
