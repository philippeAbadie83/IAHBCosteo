# utils/sty_tables.py
"""
Estilos específicos para tablas - Coherente con tbl_base.py
"""

TABLE_STYLES = """
/* ===== Contenedor QTable: no ocultar nada ===== */
.q-table__container {
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin: 16px 0;
    overflow: visible; /* importante para que se vea la paginación */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* ===== Encabezado con gradiente ===== */
.q-table thead tr {
    background: linear-gradient(135deg, #0072CE 0%, #0056b3 100%);
}
.q-table th {
    color: #fff;
    font-weight: 600;
    font-size: 14px;
    padding: 14px 16px;
    white-space: nowrap;
}

/* ===== Cuerpo ===== */
.q-table td {
    padding: 12px 16px;
    font-size: 14px;
    color: #495057;
    vertical-align: middle;
}
.q-table tbody tr:nth-child(even) { background-color: #f8f9fa; }
.q-table tbody tr:hover { background-color: #e3f2fd; }

/* ===== Badges ===== */
.value-badge {
    background-color: #e8f5e9;
    color: #2e7d32;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 600;
    display: inline-block;
}
.alert-badge {
    background-color: #ffebee;
    color: #c62828;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: 600;
    display: inline-block;
}

/* ===== Botón Exportar ===== */
.export-btn-pro {
    background: linear-gradient(135deg, #0072CE 0%, #0056b3 100%);
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-weight: 600;
    box-shadow: 0 2px 6px rgba(0,114,206,0.3);
    transition: transform .2s, box-shadow .2s;
}
.export-btn-pro:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,114,206,0.4);
}

/* ===== Contador ===== */
.result-counter-pro {
    font-size: 14px;
    color: #6c757d;
    padding: 12px 0;
    font-weight: 500;
}

/* ===== Columnas congeladas ===== */
.sticky-col {
    position: sticky;
    z-index: 2;
    background: inherit;
    box-shadow: 2px 0 4px rgba(0, 0, 0, 0.05);
}

/* ===== Responsive ===== */
@media (max-width: 1024px) {
    .q-table__container { overflow-x: auto; }
    .q-table { min-width: 1000px; }
}
"""

