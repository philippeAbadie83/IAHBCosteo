# frontend/pages/p_imp_provData.py

from nicegui import ui
import pandas as pd
import io
from datetime import date
from services.db_services import insertar_proveedor, get_proveedores_por_fecha
from core import layout
from frontend.components.tbl_base import crear_tabla


@ui.page("/importar_proveedores")
def importar_proveedores():
    """Página para importar proveedores desde archivo CSV o Excel."""

    def content():
        ui.label("Importar Proveedores desde CSV/Excel") \
            .classes("text-2xl font-bold mb-6")

        # ----------------- Handler de Upload -----------------
        def handle_upload(e):
            try:
                file_bytes = e.content.read()

                # Detectar tipo: CSV o Excel
                if e.name.endswith(".csv"):
                    df = pd.read_csv(io.BytesIO(file_bytes))
                else:
                    df = pd.read_excel(io.BytesIO(file_bytes))

                # Definir columnas requeridas
                required_cols = [
                    "Proveedor", "Multiplicador", "Valor",
                    "Flete de origen", "Arancel",
                    "Gtos aduana", "Flete Mex", "Comentarios"
                ]

                missing = [c for c in required_cols if c not in df.columns]
                if missing:
                    ui.notify(f"Error: faltan columnas → {', '.join(missing)}",
                              color="negative")
                    return

                # Renombrar columnas → BD
                df = df.rename(columns={
                    "Proveedor": "prov_name",
                    "Multiplicador": "prov_famil",
                    "Valor": "prov_multip",
                    "Flete de origen": "prov_pct_fleteorig",
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
                    data["prov_createby"] = "Philippe"
                    insertar_proveedor(data)

                ui.notify(f"{len(df)} proveedores importados correctamente ✅")

            except Exception as ex:
                ui.notify(f"Error al importar: {ex}", color="negative")

        # ----------------- Botón Upload -----------------
        ui.upload(
            on_upload=handle_upload,
            auto_upload=True,
            multiple=False,
            label="Subir archivo"
        ).classes("mb-4")

        # ----------------- Tabla de verificación -----------------
        hoy = str(date.today())
        df = get_proveedores_por_fecha(hoy)

        ui.label(f"Proveedores importados o actualizados el {hoy}") \
            .classes("text-xl font-bold mt-6 mb-4")

        if df.empty:
            ui.label("No hay registros importados/actualizados en la fecha").classes("text-gray-500")
        else:
            columnas = [
                {"name": "prov_name", "label": "Proveedor", "field": "prov_name", "sortable": True},
                {"name": "prov_famil", "label": "Familia", "field": "prov_famil"},
                {"name": "prov_multip", "label": "Valor", "field": "prov_multip"},
                {"name": "prov_pct_fleteorig", "label": "Flete Origen %", "field": "prov_pct_fleteorig"},
                {"name": "prov_pct_arancel", "label": "Arancel %", "field": "prov_pct_arancel"},
                {"name": "prov_pct_gtoaduana", "label": "Gtos Aduana %", "field": "prov_pct_gtoaduana"},
                {"name": "prov_pct_fletedest", "label": "Flete Mex %", "field": "prov_pct_fletedest"},
                {"name": "prov_coment", "label": "Comentarios", "field": "prov_coment"},
                {"name": "prov_version", "label": "Versión", "field": "prov_version"},
                {"name": "prov_createdate", "label": "Creado", "field": "prov_createdate"},
                {"name": "prov_updatedate", "label": "Actualizado", "field": "prov_updatedate"},
            ]

            crear_tabla(
                nombre="Proveedores importados",
                columnas=columnas,
                data=df,
                exportar=True,
                congelar=["prov_name", "prov_famil"]
            )

    layout.render(content)
