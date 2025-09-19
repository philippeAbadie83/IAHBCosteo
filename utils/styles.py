# utils/styles.py
from nicegui import ui

def setup_global_styles():
    """Configura estilos CSS globales para la aplicación"""
    ui.add_head_html('''
    <style>


    /* --- HEADER FIJADO CORRECTAMENTE --- */
    .q-header {
        background: linear-gradient(90deg, #0056b3 0%, #0072CE 100%);
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 56px;
        z-index: 2000; /* Mayor que el sidebar */
    }

    /* --- SIDEBAR DEBAJO DEL HEADER --- */
    .q-drawer {
        top: 56px !important;
        height: calc(100% - 56px) !important;
        z-index: 1000;
    }

    /* --- CONTENIDO PRINCIPAL AJUSTADO --- */
    .q-page-container {
        padding-top: 56px !important;
        margin-left: 240px;
        transition: margin-left 0.3s ease;
        min-height: calc(100vh - 56px);
    }

    .q-drawer--mini ~ .q-page-container {
        margin-left: 64px;
    }

    /* --- HEADER ESPECÍFICO DE TU APP --- */
    .header-custom {
        background: linear-gradient(90deg, #0056b3 0%, #0072CE 100%);
        color: white;
        height: 56px;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 2000;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }

    /* Botón de toggle del sidebar */
    .sidebar-toggle-btn {
        transition: transform 0.3s ease;
    }
    .sidebar-toggle-btn:hover {
        transform: scale(1.1);
        background-color: #e3f2fd !important;
    }

    /* Cuando el sidebar está mini, gira el ícono */
    .q-drawer--mini .sidebar-toggle-btn .q-icon {
        transform: rotate(180deg);
    }

    /* Mejora visual para el header del sidebar */
    .sidebar-header {
        background-color: #f8f9fa;
    }


    /* Estilos para tablas */
    .sticky-header .q-table__top {
        position: sticky;
        top: 0;
        z-index: 1000;
        background: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }

    .full-width {
        width: 100% !important;
    }

    .data-table-card {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        margin: 16px 0;
    }

    .q-table th {
        font-weight: 600;
        background-color: #f8f9fa;
        font-size: 14px;
        color: #374151;
    }

    .q-table td {
        font-size: 14px;
        padding: 12px 16px;
    }

    .q-table tr:nth-child(even) {
        background-color: #fafafa;
    }

    .q-table tr:hover {
        background-color: #e3f2fd !important;
        transition: background-color 0.2s ease;
    }

    /* Sidebar para ampliar o minimizar */
    .q-drawer--mini .q-btn__content .q-btn__label { display: none; }
    .q-drawer--mini .q-btn { justify-content: center; }

    .q-header {
        background: linear-gradient(90deg, #0056b3 0%, #0072CE 100%);
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }

    .q-drawer .section-label {
        font-size: 11px;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #6b7280;
        padding-left: 12px;
        margin-top: 6px;
        margin-bottom: 2px;
        background-color: #f9fafb;
        border-right: 1px solid #e5e7eb;
    }

    .q-drawer .q-btn {
        transition: background-color 0.2s ease;
    }
    .q-drawer .q-btn:hover {
        background-color: #e3f2fd;
    }

    .q-btn .q-icon {
        color: #0072CE !important;
    }

    .q-table tr:hover td {
        background-color: #e3f2fd !important;
        cursor: pointer;
    }
    .q-table tr:active {
        background-color: #bbdefb !important;
    }

    .action-btn {
        margin: 0 2px;
        transition: transform 0.2s ease;
    }
    .action-btn:hover {
        transform: scale(1.1);
    }

    /* Mejoras generales de UI */
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

    /* --- FIX: Sidebar debajo del header --- */
    .q-drawer {
        top: 56px !important;   /* altura del header */
        height: calc(100% - 56px) !important;
    }

    /* --- FIX: Ajustar contenido cuando sidebar está abierto --- */
    .q-page-container {
        margin-left: 240px;   /* ancho drawer normal */
        transition: margin-left 0.3s ease;
        padding: 16px;
    }
    .q-drawer--mini ~ .q-page-container {
        margin-left: 64px;    /* ancho drawer mini */
    }

    /* Responsive */
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
            margin-left: 0 !important;  /* en móvil el drawer es overlay */
        }
    }
    </style>
    ''')
