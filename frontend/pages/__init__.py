# Hidrobart Costeo
# frontend/pages/__init__.py
# Marca este directorio como un paquete Python y permite la carga automática de páginas

import importlib
import pkgutil

def auto_import_pages():
    """Importa automáticamente todos los módulos en este paquete y muestra un log en consola"""
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        full_module = f"{__name__}.{module_name}"
        importlib.import_module(full_module)
        print(f"[pages] ✅ Página registrada: {full_module}")

# Ejecutar importación automática al cargar el paquete
auto_import_pages()
