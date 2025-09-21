# Hidrobart Costeo
# frontend/pages/p_imp_provData.py
#
# Página: Importar Proveedores desde CSV/Excel
# Funcionalidad:
# - Permite subir archivo CSV o Excel.
# - Valida columnas requeridas.
# - Limpia valores nulos (NaN) para evitar errores SQL.
# - Inserta cada fila en la BD con autor fijo "Philippe Abadie".
# - Se integra al layout general de la aplicación.

from nicegui import ui
import pandas as pd
import io
from datetime import date
from services.db_services import insertar_proveedor, get_proveedores_por_fecha
from utils.helpers import sanitize_dataframe
from frontend.components.tbl_base import crear_tabla
from core import layout


@ui.page("/importar_proveedores")
def importar_proveedores():
    """Página para importar proveedores desde archivo CSV o Excel."""

    def content():
        ui.label("Importar Proveedores desde CSV/Excel") \
            .classes("text-2xl font-bold mb-6")

        tabla_container = ui.column().classes("w-full mt-6")

        def mostrar_importados():
            """Dibuja tabla con registros importados hoy"""
            hoy = date.today().strftime("%Y-%m-%d")
            df: pd.DataFrame = get_proveedores_por_fecha(hoy)
            df = sanitize_dataframe(df)

            tabla_container.clear()

            if df.empty:
                with tabla_container:
                    ui.label(f"No hay registros importados el {hoy}")
                return

            columnas = [
                {"name": "proveedor", "label": "Proveedor", "field": "proveedor", "sortable": True, "align": "left"},
                {"name": "familia", "label": "Familia", "field": "familia", "sortable": True, "align": "left"},
                {"name": "valor", "label": "Valor", "field": "valor", "align": "right"},
                {"name": "flete_origen", "label": "Flete Origen %", "field": "flete_origen", "align": "right"},
                {"name": "arancel", "label": "Arancel %", "field": "arancel", "align": "right"},
                {"name": "gtos_aduana", "label": "Gtos Aduana %", "field": "gtos_aduana", "align": "right"},
                {"name": "flete_mex", "label": "Flete Mex %", "field": "flete_mex", "align": "right"},
                {"name": "total_gastos", "label": "Total Gastos %", "field": "total_gastos", "align": "right"},
                {"name": "comentarios", "label": "Comentarios", "field": "comentarios", "align": "left"},
                {"name": "version", "label": "Versión", "field": "version", "align": "center"},
                {"name": "fecha_update", "label": "Última Actualización", "field": "fecha_update", "align": "center"},
                {"name": "usuario_update", "label": "Actualizado por", "field": "usuario_update", "align": "left"},
            ]

            formatos_especiales = {
                'flete_origen': {'tipo': 'porcentaje'},
                'arancel': {'tipo': 'porcentaje'},
                'gtos_aduana': {'tipo': 'porcentaje'},
                'flete_mex': {'tipo': 'porcentaje'},
                'total_gastos': {'tipo': 'porcentaje'}
            }

            with tabla_container:
                crear_tabla(
                    nombre=f"Proveedores importados el {hoy}",
                    columnas=columnas,
                    data=df,
                    exportar=True,
                    congelar=["proveedor", "familia"],
                    formatos_especiales=formatos_especiales
                )

        def handle_upload(e):
            try:
                file_bytes = e.content.read()

                if e.name.endswith(".csv"):
                    df = pd.read_csv(io.BytesIO(file_bytes))
                else:
                    df = pd.read_excel(io.BytesIO(file_bytes))

                required_cols = [
                    "Proveedor",
                    "Multiplicador",
                    "Valor",
                    "Flete de orígen",
                    "Arancel",
                    "Gtos aduana",
                    "Flete Mex",
                    "Comentarios",
                ]

                missing = [c for c in required_cols if c not in df.columns]
                if missing:
                    ui.notify(f"Error: faltan columnas → {', '.join(missing)}", color="negative")
                    return

                df = df.rename(columns={
                    "Proveedor": "prov_name",
                    "Multiplicador": "prov_famil",
                    "Valor": "prov_multip",
                    "Flete de orígen": "prov_pct_fleteorig",
                    "Arancel": "prov_pct_arancel",
                    "Gtos aduana": "prov_pct_gtoaduana",
                    "Flete Mex": "prov_pct_fletedest",
                    "Comentarios": "prov_coment",
                })

                df = df.fillna({
                    "prov_coment": "",
                    "prov_multip": 0,
                    "prov_pct_fleteorig": 0,
                    "prov_pct_arancel": 0,
                    "prov_pct_gtoaduana": 0,
                    "prov_pct_fletedest": 0,
                })

                for _, row in df.iterrows():
                    data = row.to_dict()
                    data["prov_createby"] = "Philippe Abadie"
                    insertar_proveedor(data)

                ui.notify(f"{len(df)} proveedores importados correctamente ✅")
                mostrar_importados()

            except Exception as ex:
                ui.notify(f"Error al importar: {ex}", color="negative")

        ui.upload(
            on_upload=handle_upload,
            auto_upload=True,
            multiple=False,
            label="Subir archivo"
        ).classes("mb-4")

        # Mostrar registros de hoy al abrir
        mostrar_importados()

    layout.render(content)

