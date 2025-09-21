


# Estilos específicos para tablas profesionales
TABLE_STYLES = """
/* --- TABLA PROFESIONAL CORPORATIVA --- */
.pro-table-container {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    margin: 16px 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.pro-table {
    width: 100%;
    border-collapse: collapse;
}

.pro-table thead tr {
    background: linear-gradient(135deg, #0072CE 0%, #0056b3 100%);
}

.pro-table th {
    color: white;
    font-weight: 600;
    font-size: 14px;
    padding: 14px 16px;
    text-align: left;
    position: relative;
    white-space: nowrap;
}

.pro-table th:after {
    content: '';
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
    height: 60%;
    width: 1px;
    background: rgba(255, 255, 255, 0.2);
}

.pro-table th:last-child:after {
    display: none;
}

.pro-table tbody tr {
    transition: background-color 0.2s ease;
    border-bottom: 1px solid #e9ecef;
}

.pro-table tbody tr:nth-child(even) {
    background-color: #f8f9fa;
}

.pro-table tbody tr:hover {
    background-color: #e3f2fd;
    cursor: pointer;
}

.pro-table td {
    padding: 12px 16px;
    font-size: 14px;
    color: #495057;
    vertical-align: middle;
}

/* Badges para valores importantes */
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

/* Progress bars para porcentajes */
.percentage-bar {
    height: 6px;
    background-color: #e9ecef;
    border-radius: 3px;
    overflow: hidden;
    margin-top: 4px;
}

.percentage-fill {
    height: 100%;
    background: linear-gradient(90deg, #0072CE 0%, #00A0E3 100%);
    border-radius: 3px;
}

/* Botones de acción */
.action-btn {
    transition: all 0.2s ease;
    border-radius: 6px;
    padding: 6px;
    margin: 0 2px;
}

.action-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background-color: #e3f2fd;
}

/* Filtros mejorados */
.pro-filter {
    background-color: white;
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    border: 1px solid #e9ecef;
}

.pro-filter .q-field__control {
    height: 42px;
    border-radius: 6px;
    border: 1px solid #dee2e6;
}

.pro-filter .q-field__control:hover {
    border-color: #0072CE;
}

.pro-filter .q-field__label {
    color: #6c757d;
    font-weight: 500;
}

/* Botón de exportar mejorado */
.export-btn-pro {
    background: linear-gradient(135deg, #0072CE 0%, #0056b3 100%);
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-weight: 600;
    transition: all 0.2s ease;
    box-shadow: 0 2px 6px rgba(0, 114, 206, 0.3);
}

.export-btn-pro:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 114, 206, 0.4);
}

/* Contador de resultados */
.result-counter-pro {
    font-size: 14px;
    color: #6c757d;
    padding: 12px 0;
    font-weight: 500;
}

/* Columnas congeladas mejoradas */
.sticky-col {
    position: sticky;
    z-index: 2;
    background: inherit;
    box-shadow: 2px 0 4px rgba(0, 0, 0, 0.05);
}

.sticky-proveedor {
    left: 0;
}

.sticky-familia {
    left: 200px; /* Ajustar según el ancho de la columna proveedor */
}

/* Responsive */
@media (max-width: 1024px) {
    .pro-table-container {
        overflow-x: auto;
    }

    .pro-table {
        min-width: 1000px;
    }

    .pro-filter {
        flex-direction: column;
    }

    .pro-filter .q-field {
        margin-bottom: 12px;
    }
}

/* Tooltips personalizados */
.custom-tooltip {
    background-color: #495057;
    color: white;
    padding: 6px 12px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 500;
}


/* ENCABEZADO AZUL CON LETRAS BLANCAS */
.pro-table thead tr {
    background: linear-gradient(135deg, #0072CE 0%, #0056b3 100%) !important;
}

.pro-table th {
    color: white !important;
    font-weight: 600 !important;
    font-size: 14px !important;
}

.pro-table th .q-table__sort-icon {
    color: white !important;
}

/* Badges corregidos */
.value-badge, .alert-badge {
    padding: 4px 8px !important;
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

/* Botón de exportar */
.export-btn-pro {
    background: linear-gradient(135deg, #0072CE 0%, #0056b3 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 10px 20px !important;
    font-weight: 600 !important;
}

/* Zebra striping */
.pro-table tbody tr:nth-child(even) {
    background-color: #f8f9fa !important;
}

.pro-table tbody tr:hover {
    background-color: #e3f2fd !important;
}

