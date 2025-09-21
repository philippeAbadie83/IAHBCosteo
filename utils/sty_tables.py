# utils/sty_tables.py
"""
Estilos específicos para tablas - Coherente con tbl_base.py
"""

TABLE_STYLES = """
/* --- CONTENEDOR PRINCIPAL --- */
.pro-table-container {
    border-radius: 8px !important;
    overflow: hidden !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
    margin: 16px 0 !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
}

/* --- TABLA PROFESIONAL --- */
.pro-table {
    width: 100% !important;
    border-collapse: collapse !important;
}

/* ENCABEZADO AZUL CON LETRAS BLANCAS */
.pro-table thead tr {
    background: linear-gradient(135deg, #0072CE 0%, #0056b3 100%) !important;
}

.pro-table th {
    color: white !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 14px 16px !important;
    text-align: left !important;
    position: relative !important;
    white-space: nowrap !important;
}

/* Separadores entre columnas del header */
.pro-table th:after {
    content: '' !important;
    position: absolute !important;
    right: 0 !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    height: 60% !important;
    width: 1px !important;
    background: rgba(255, 255, 255, 0.2) !important;
}

.pro-table th:last-child:after {
    display: none !important;
}

/* CUERPO DE LA TABLA */
.pro-table tbody tr {
    transition: background-color 0.2s ease !important;
    border-bottom: 1px solid #e9ecef !important;
}

/* Zebra striping */
.pro-table tbody tr:nth-child(even) {
    background-color: #f8f9fa !important;
}

/* Efecto hover */
.pro-table tbody tr:hover {
    background-color: #e3f2fd !important;
    cursor: pointer !important;
}

.pro-table td {
    padding: 12px 16px !important;
    font-size: 14px !important;
    color: #495057 !important;
    vertical-align: middle !important;
}

/* --- BADGES PARA PORCENTAJES --- */
.value-badge, .alert-badge {
    padding: 4px 10px !important;
    border-radius: 12px !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    display: inline-block !important;
}

.value-badge {
    background-color: #e8f5e9 !important;
    color: #2e7d32 !important;
}

.alert-badge {
    background-color: #ffebee !important;
    color: #c62828 !important;
}

/* --- FILTROS --- */
.pro-filter {
    background-color: white !important;
    border-radius: 8px !important;
    padding: 16px !important;
    margin-bottom: 16px !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05) !important;
    border: 1px solid #e9ecef !important;
}

/* --- BOTÓN EXPORTAR --- */
.export-btn-pro {
    background: linear-gradient(135deg, #0072CE 0%, #0056b3 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 10px 20px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 6px rgba(0, 114, 206, 0.3) !important;
}

.export-btn-pro:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 8px rgba(0, 114, 206, 0.4) !important;
}

/* --- CONTADOR RESULTADOS --- */
.result-counter-pro {
    font-size: 14px !important;
    color: #6c757d !important;
    padding: 12px 0 !important;
    font-weight: 500 !important;
}

/* --- COLUMNAS CONGELADAS --- */
.sticky-col {
    position: sticky !important;
    z-index: 2 !important;
    background: inherit !important;
    box-shadow: 2px 0 4px rgba(0, 0, 0, 0.05) !important;
}

/* --- RESPONSIVE --- */
@media (max-width: 1024px) {
    .pro-table-container {
        overflow-x: auto !important;
    }

    .pro-table {
        min-width: 1000px !important;
    }

    .pro-filter {
        flex-direction: column !important;
    }
}


/* --- SOBRESCRIBIR COMPLETAMENTE QUASAR --- */

/* Contenedor principal */
.q-table__container {
    border-radius: 8px !important;
    overflow: hidden !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
    margin: 16px 0 !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
}

/* Encabezado azul */
.q-table thead tr {
    background: linear-gradient(135deg, #0072CE 0%, #0056b3 100%) !important;
}

.q-table th {
    color: white !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 14px 16px !important;
}

/* Zebra striping */
.q-table tbody tr:nth-child(even) {
    background-color: #f8f9fa !important;
}

.q-table tbody tr:hover {
    background-color: #e3f2fd !important;
}

.q-table td {
    padding: 12px 16px !important;
    font-size: 14px !important;
    color: #495057 !important;
}

/* Badges - ESTOS SÍ funcionarán */
.value-badge {
    background-color: #e8f5e9 !important;
    color: #2e7d32 !important;
    padding: 4px 10px !important;
    border-radius: 12px !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    display: inline-block !important;
}

.alert-badge {
    background-color: #ffebee !important;
    color: #c62828 !important;
    padding: 4px 10px !important;
    border-radius: 12px !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    display: inline-block !important;
}


"""