# utils/sty_navigation.py
"""
Estilos específicos para navegación - Drawer, Header, Estados Activos
"""
NAVIGATION_STYLES = """
/* ===== HEADER PROFESIONAL ===== */
.q-header {
    background: linear-gradient(135deg, #1e40af 0%, #3b82f6 50%, #60a5fa 100%) !important;
    box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3) !important;
    height: 64px !important;
}

.header-title {
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    text-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
}

.menu-toggle-btn {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    border-radius: 12px !important;
}

.menu-toggle-btn:hover {
    background: rgba(255,255,255,0.15) !important;
    transform: scale(1.05) !important;
}

.system-menu-btn {
    background: rgba(255,255,255,0.1) !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-radius: 8px !important;
    transition: all 0.3s ease !important;
}

.system-menu-btn:hover {
    background: rgba(255,255,255,0.2) !important;
    transform: translateY(-2px) !important;
}

/* ===== DRAWER PROFESIONAL ===== */
.q-drawer--left {
    background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%) !important;
    border-right: 1px solid #e2e8f0 !important;
    box-shadow: 4px 0 15px rgba(0,0,0,0.1) !important;
    transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* ===== MODO COLAPSADO ===== */
.q-drawer--mini {
    width: 72px !important;
}

.q-drawer--mini .nav-item-text,
.q-drawer--mini .section-title {
    display: none !important;
}

.q-drawer--mini .q-expansion-item__content {
    display: none !important;
}

.q-drawer--mini .q-btn {
    justify-content: center !important;
    min-width: 48px !important;
}

/* ===== HEADER DEL DRAWER ===== */
.drawer-header {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%) !important;
    border-bottom: 2px solid #e2e8f0 !important;
    padding: 16px !important;
}

.collapse-btn {
    transition: all 0.3s ease !important;
    border-radius: 50% !important;
    background: rgba(59, 130, 246, 0.1) !important;
}

.collapse-btn:hover {
    background: rgba(59, 130, 246, 0.2) !important;
    transform: scale(1.1) rotate(180deg) !important;
}

/* ===== SECCIONES DEL MENU ===== */
.q-expansion-item {
    background: rgba(255,255,255,0.7) !important;
    border: 1px solid rgba(226,232,240,0.5) !important;
    border-radius: 12px !important;
    margin-bottom: 12px !important;
    backdrop-filter: blur(5px) !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
}

.q-expansion-item:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
}

.q-expansion-item__header {
    font-weight: 600 !important;
    color: #334155 !important;
}

/* ===== ITEMS DE NAVEGACION ===== */
.nav-item {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    border-radius: 8px !important;
    margin: 2px 8px !important;
    position: relative !important;
    overflow: hidden !important;
}

.nav-item:hover {
    background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%) !important;
    transform: translateX(4px) !important;
    box-shadow: 0 2px 8px rgba(59, 130, 246, 0.2) !important;
}

/* ===== ESTADO ACTIVO (ROJO) ===== */
.nav-item-active {
    background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%) !important;
    color: #dc2626 !important;
    font-weight: 600 !important;
    transform: translateX(6px) !important;
    box-shadow: 0 2px 12px rgba(220, 38, 38, 0.2) !important;
    border-left: 4px solid #dc2626 !important;
    border-radius: 0 8px 8px 0 !important;
}

.nav-item-active:hover {
    background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%) !important;
    transform: translateX(6px) !important;
    box-shadow: 0 4px 16px rgba(220, 38, 38, 0.3) !important;
}

.nav-item-active .q-btn__content {
    color: #dc2626 !important;
}

/* ===== CONTENIDO PRINCIPAL ===== */
.q-page-container {
    padding-top: 64px !important;
    padding-left: 280px !important;
    transition: padding-left 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    background: linear-gradient(135deg, #fafafa 0%, #f5f5f5 100%) !important;
}

.content-collapsed {
    padding-left: 72px !important;
}

/* ===== RESPONSIVE ===== */
@media (max-width: 1024px) {
    .q-page-container {
        padding-left: 16px !important;
    }

    .q-drawer--left {
        position: fixed !important;
        z-index: 1500 !important;
    }
}

/* ===== FOOTER PROFESIONAL ===== */
.q-footer {
    background: linear-gradient(135deg, #1f2937 0%, #374151 100%) !important;
    border-top: 1px solid #4b5563 !important;
}
"""