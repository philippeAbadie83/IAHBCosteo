# app.py

from sys import implementation
from core.__version__ import __version__, __build__
print(f"Versión: {__version__}, Build: {__build__}")

from nicegui import ui
from core import layout
from utils import styles

# Importar páginas reales
import frontend.pages.v_tblprov_data
import frontend.pages.p_imp_provData
import frontend.pages.ttbl
import frontend.pages.ttbl2
import frontend.pages.ttbl_pipeline
import frontend.pages.test_tbl_simple  # ✅ CORRECTO
import frontend.pages.test_tbl_sample  # ✅ CORRECTO
import frontend.pages.test_fix
import frontend.pages.test_minimal
import frontend.pages.test_table
import frontend.pages.v_tblprov_data_fixed



# Importar placeholders (👉 muy importante)
import frontend.pages.placeholders


@ui.page('/')
def index_page():
    layout.render()


if __name__ in ["__main__", "__mp_main__"]:
    styles.setup_global_styles()
    ui.run(
        title=f"AIHB-Costeo v{__version__}",
        reload=True,
        port=5858,
        host="0.0.0.0",
        show=False
    )
