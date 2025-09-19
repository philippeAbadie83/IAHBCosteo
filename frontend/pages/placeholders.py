# frontend/pages/placeholders.py
from nicegui import ui
from core import layout

# ---------- Proveedores ----------
@ui.page('/v_tblprov_all')
def proveedores_todos():
    layout.render(lambda: ui.label('📦 Placeholder: Proveedores (activos y no activos)'))

# ---------- Productos ----------
@ui.page('/productos/listado')
def productos_listado():
    layout.render(lambda: ui.label('📦 Placeholder: Listado de Productos'))

@ui.page('/productos/importar')
def productos_importar():
    layout.render(lambda: ui.label('📦 Placeholder: Importar Productos'))

@ui.page('/productos/precios-proveedor')
def precios_proveedor():
    layout.render(lambda: ui.label('📦 Placeholder: Precios de Proveedores'))

@ui.page('/productos/carga-precios')
def carga_precios():
    layout.render(lambda: ui.label('📦 Placeholder: Carga de Precios Nuevos'))

@ui.page('/productos/costo-destino')
def productos_costeo():
    layout.render(lambda: ui.label('📦 Placeholder: Cálculo de Costeo'))

@ui.page('/productos/lista-precios')
def lista_precios():
    layout.render(lambda: ui.label('📦 Placeholder: Lista de Precios'))

# ---------- Kit Productos ----------
@ui.page('/kit/listado')
def kit_listado():
    layout.render(lambda: ui.label('📦 Placeholder: Listado de Productos (Kit)'))

@ui.page('/kit/armado')
def kit_armado():
    layout.render(lambda: ui.label('📦 Placeholder: Armado de Kit'))

@ui.page('/kit/costeo')
def kit_costeo():
    layout.render(lambda: ui.label('📦 Placeholder: Costeo de Kit'))

# ---------- Simulaciones ----------
@ui.page('/sim/clientes-especiales')
def sim_clientes():
    layout.render(lambda: ui.label('📦 Placeholder: Clientes Especiales'))

@ui.page('/sim/campana')
def sim_campana():
    layout.render(lambda: ui.label('📦 Placeholder: Campaña'))

@ui.page('/sim/mejores-productos')
def sim_mejores_productos():
    layout.render(lambda: ui.label('📦 Placeholder: Mejores Productos'))

@ui.page('/sim/mejores-margenes')
def sim_mejores_margenes():
    layout.render(lambda: ui.label('📦 Placeholder: Mejores Márgenes'))
