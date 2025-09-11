# Hidrobart Costeo
# frontend/pages/__init__.py

import importlib
import pkgutil

def auto_import_pages():
    """Importa automáticamente todos los módulos en este paquete y muestra un log en consola"""
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        if module_name == "__init__":   # << evita recursión
            continue
        full_module = f"{__name__}.{module_name}"
        importlib.import_module(full_module)
        print(f"[pages] ✅ Página registrada: {full_module}")

# Ejecutar importación automática al cargar el paquete
auto_import_pages()
