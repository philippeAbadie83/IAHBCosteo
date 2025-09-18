# app.py

from core.__version__ import __version__, __build__
print(f"Versión: {__version__}, Build: {__build__}")

from nicegui import ui
from core import layout

# Importar páginas reales
import frontend.pages.v_tblprov_data
import frontend.pages.p_imp_provData
import frontend.pages.ttbl
import frontend.pages.ttbl2
import frontend.pages.ttbl_pipeline


# Estilos globales
def setup_global_styles():
    ui.add_head_html('''
    <style>
    .bg-gradient-hydro { background: linear-gradient(135deg, #0072CE 0%, #00A0E3 100%); }
    .cost-card { border-radius: 12px; box-shadow: 0 4px 15px rgba(0, 114, 206, 0.15); transition: transform 0.2s ease; }
    .cost-card:hover { transform: translateY(-2px); }
    .q-table th { background-color: #f0f8ff !important; color: #0072CE !important; font-weight: 600; }
    .q-table tr:nth-child(even) { background-color: #fafafa; }
    .q-table tr:hover { background-color: #e3f2fd !important; }
    </style>
    ''')


@ui.page('/')
def index_page():
    layout.render()   # 👉 vacío, solo layout y mensaje si quieres


if __name__ in ["__main__", "__mp_main__"]:
    setup_global_styles()
    ui.run(title="AIHB-Costeo", reload=False, port=5858, host="0.0.0.0")
