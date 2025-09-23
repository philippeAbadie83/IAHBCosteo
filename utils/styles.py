# utils/styles.py
from nicegui import ui
from nicegui import ui
from utils.sty_tables import TABLE_STYLES

GLOBAL_STYLES = """
/* ===== Header (simple y seguro) ===== */
.q-header, .header-custom {
    background: linear-gradient(90deg, #0056b3 0%, #0072CE 100%);
    height: 56px;
}

/* ===== Drawer (solo anchos) ===== */
.q-drawer:not(.q-drawer--mini) { width: 240px; }
.q-drawer--mini { width: 64px; }

/* ===== Page container (compensa header fijo del layout) ===== */
.q-page-container {
    padding-top: 56px;
    padding-left: 16px;
    padding-right: 16px;
    min-height: calc(100vh - 56px);
}

/* ===== Botón del header con z-index seguro ===== */
.q-header .q-btn { z-index: 10; }

/* ===== Responsive ===== */
@media (max-width: 768px) {
    .q-page-container { padding: 12px 8px; }
    .q-drawer:not(.q-drawer--mini) { width: 220px; }
}
"""

def setup_global_styles() -> None:
    """Inyecta estilos globales (header/drawer) + tablas."""
    ui.add_head_html(f'<style>{GLOBAL_STYLES}{TABLE_STYLES}</style>')

def apply_table_styles() -> None:
    """Estilos de tabla ya se aplican globalmente."""
    pass
