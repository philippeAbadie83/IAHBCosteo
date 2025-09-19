# DeepSeek
# utils/styles.py CSS

from nicegui import ui

def setup_global_styles():
    """Configura estilos CSS globales para la aplicación"""
    ui.add_head_html('''
    <style>
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

     /* Sidebar para ampliar o minimizar 20250919 */
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
        padding-left: 12px;   /* 👉 añade consistencia */
        margin-top: 6px;
        margin-bottom: 2px;
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

    .q-drawer .section-label {
        font-size: 11px;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #6b7280; /* gris medio */
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

    /* Costeo Card? */

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

    }
    </style>
    ''')