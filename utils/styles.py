# utils/styles.py
from nicegui import ui
from nicegui import ui
from utils.sty_tables import TABLE_STYLES

# Estilos globales para toda la aplicación
GLOBAL_STYLES = """
/* --- ESTILOS PRINCIPALES --- */
.q-header, .header-custom {
    background: linear-gradient(90deg, #0056b3 0%, #0072CE 100%) !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2) !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    height: 56px !important;
    z-index: 3000 !important;
}

/* --- COMPORTAMIENTO DEL DRAWER --- */
.q-drawer {
    position: fixed !important;
    transform: none !important;
    top: 56px !important;
    height: calc(100% - 56px) !important;
    z-index: 2000 !important;
    background-color: #f8f9fa !important;
    box-shadow: 2px 0 8px rgba(0,0,0,0.1) !important;
    left: 0 !important;
}

    /* Drawer normal (expandido) */
    .q-drawer:not(.q-drawer--mini) {
        width: 240px !important;
    }

    /* Drawer mini */
    .q-drawer--mini {
        width: 64px !important;
    }

    /* Eliminar cualquier transformación que pueda ocultar el drawer */
    .q-drawer--mini, .q-drawer:not(.q-drawer--mini) {
        transform: translateX(0) !important;
    }

    /* Asegurar que el backdrop no interfiera */
    .q-drawer__backdrop {
        display: none !important;
    }

    /* Contenido principal se ajusta al drawer */
    .q-page-container {
        padding-top: 56px !important;
        margin-left: 240px;
        transition: margin-left 0.3s ease;
        min-height: calc(100vh - 56px);
        padding: 16px;
    }

    .q-drawer--mini ~ .q-page-container {
        margin-left: 64px;
    }

    /* BOTONES DEL HEADER */
    .q-header .q-btn {
        z-index: 4000 !important;
    }

    /* --- ESTILOS ESPECÍFICOS DE LA APP --- */
    .sidebar-toggle-btn {
        transition: transform 0.3s ease;
    }
    .sidebar-toggle-btn:hover {
        transform: scale(1.1);
        background-color: #e3f2fd !important;
    }

    .q-drawer--mini .sidebar-toggle-btn .q-icon {
        transform: rotate(180deg);
    }

    .sidebar-header {
        background-color: #f8f9fa;
        border-bottom: 1px solid #e5e7eb !important;
    }

    .section-label {
        font-size: 11px !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
        color: #6b7280 !important;
        padding-left: 12px !important;
        margin-top: 6px !important;
        margin-bottom: 2px !important;
        background-color: #f9fafb !important;
    }

    .q-drawer .q-btn {
        transition: background-color 0.2s ease;
        justify-content: flex-start !important;
    }
    .q-drawer .q-btn:hover {
        background-color: #e3f2fd !important;
    }

    .q-btn .q-icon {
        color: #0072CE !important;
    }

    /* Sidebar mini - ocultar labels */
    .q-drawer--mini .q-btn__content .q-btn__label {
        display: none !important;
    }
    .q-drawer--mini .q-btn {
        justify-content: center !important;
    }

    /* Elementos que se ocultan en modo mini */
    .mini-hidden {
        transition: opacity 0.3s ease;
    }

    .q-drawer--mini .mini-hidden {
        opacity: 0;
        height: 0;
        padding: 0;
        margin: 0;
        overflow: hidden;
    }

    .q-drawer--mini .q-icon {
        opacity: 1 !important;
        visibility: visible !important;
    }

    .q-drawer--mini .q-expansion-item {
        min-height: 48px;
    }

    .q-drawer--mini .q-expansion-item__content {
        display: none !important;
    }

    .q-drawer--mini .q-btn {
        min-width: 48px !important;
        justify-content: center !important;
        padding: 0 !important;
    }

    .q-drawer--mini .sidebar-header {
        min-height: 48px;
        padding: 8px 4px !important;
        justify-content: center !important;
    }

    .q-drawer--mini .sidebar-header .q-btn {
        margin: 0 auto;
    }

    /* --- ESTILOS GENERALES DE UI --- */
    .bg-gradient-to-r {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .rounded-lg {
        border-radius: 12px;
    }

    .shadow-lg {
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }

    .bg-gradient-hydro {
        background: linear-gradient(135deg, #0072CE 0%, #00A0E3 100%);
    }

    .cost-card {
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 114, 206, 0.15);
        transition: all 0.3s ease;
    }

    .cost-card:hover {
        transform: translateY(-2px);
    }

    /* --- RESPONSIVE --- */
    @media (max-width: 768px) {
        .q-table {
            font-size: 12px;
        }

    .q-table th,
    .q-table td {
        padding: 8px 12px;
    }

    .q-drawer--mini {
        width: 56px !important;
    }

    .q-page-container {
        margin-left: 0 !important;
        padding: 16px 8px;
    }

    .q-drawer--mini ~ .q-page-container {
        margin-left: 0 !important;
    }

    .q-drawer {
        width: 280px !important;
        transform: translateX(-100%);
        transition: transform 0.3s ease;
    }

    .q-drawer--on-top {
        transform: translateX(0);
    }
}

/* --- MEJORAS DE VISUALIZACIÓN --- */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

* {
    transition: background-color 0.2s ease, transform 0.2s ease;
}
"""



def setup_global_styles():
    """Configura todos los estilos CSS globales para la aplicación"""
    ui.add_head_html(f'<style>{GLOBAL_STYLES}{TABLE_STYLES}</style>')

def apply_table_styles():
    """Aplica estilos para tablas"""
    # Los estilos ya están aplicados globalmente
    pass