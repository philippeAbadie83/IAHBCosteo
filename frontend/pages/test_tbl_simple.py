# frontend/pages/test_tbl_simple.py

from nicegui import ui
import pandas as pd
from frontend.components.tbl_base_simple import crear_tabla_simple
from core import layout


@ui.page("/test_tbl_simple")
def test_tabla_simple():
    def content():
        ui.label("🔧 TEST TABLA SIMPLE").classes("text-3xl font-bold mb-6")

        # ======== DATOS DE PRUEBA SIMPLES ========
        datos_prueba = [
            {"id": 1, "proveedor": "ProveedorA", "familia": "FamiliaX", "valor": 1.25},
            {"id": 2, "proveedor": "ProveedorB", "familia": "FamiliaY", "valor": 2.50},
            {"id": 3, "proveedor": "ProveedorC", "familia": "FamiliaZ", "valor": 3.75},
            {"id": 4, "proveedor": "ProveedorD", "familia": "FamiliaW", "valor": 4.00},
            {"id": 5, "proveedor": "ProveedorE", "familia": "FamiliaV", "valor": 5.25},
        ]

        df = pd.DataFrame(datos_prueba)

        # ======== COLUMNAS SIMPLES ========
        columnas = [
            {"name": "id", "label": "ID", "field": "id", "sortable": True, "align": "left"},
            {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True, "align": "left"},
            {"name": "familia", "label": "Familia", "field": "familia", "sortable": True, "align": "left"},
            {"name": "valor", "label": "Valor", "field": "valor", "sortable": True, "align": "right"},
        ]

        # ======== PRUEBA 1: Con row_key="id" ========
        ui.label("PRUEBA 1: row_key='id'").classes("text-xl font-bold mt-6 mb-2")
        crear_tabla_simple(
            nombre="Tabla Simple - Test 1",
            columnas=columnas,
            data=df,
            row_key="id"
        )

        # ======== PRUEBA 2: Con row_key="proveedor" ========
        ui.label("PRUEBA 2: row_key='proveedor'").classes("text-xl font-bold mt-6 mb-2")
        crear_tabla_simple(
            nombre="Tabla Simple - Test 2",
            columnas=columnas,
            data=df,
            row_key="proveedor"
        )

        # ======== PRUEBA 3: Con datos reales de proveedores ========
        ui.label("PRUEBA 3: Datos reales").classes("text-xl font-bold mt-6 mb-2")
        ui.label("(Se reactivará cuando solucionemos el problema de Timestamps)")

        # Importar la función real
    #    from services.db_services import get_proveedores_activos

     #   try:
     #       df_real = get_proveedores_activos()
     #       ui.label(f"✅ Datos reales cargados: {len(df_real)} registros, columnas: {list(df_real.columns)}")

            # Columnas para datos reales
      #      columnas_reales = [
      #          {"name": "id", "label": "ID", "field": "id", "sortable": True, "align": "left"},
      #          {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True, "align": "left"},
      #          {"name": "familia", "label": "Familia", "field": "familia", "sortable": True, "align": "left"},
      #          {"name": "valor", "label": "Valor", "field": "valor", "sortable": True, "align": "right"},
      #      ]

      #      crear_tabla_simple(
      #          nombre="Proveedores Reales",
      #          columnas=columnas_reales,
      #          data=df_real,
      #          row_key="id"
      #     )

       # except Exception as e:
       #     ui.label(f"❌ Error cargando datos reales: {e}").classes("text-red-500")

    layout.render(content)