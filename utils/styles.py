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

    /* Responsive */
    @media (max-width: 768px) {
        .q-table {
            font-size: 12px;
        }

        .q-table th,
        .q-table td {
            padding: 8px 12px;
        }
    }
    </style>
    ''')