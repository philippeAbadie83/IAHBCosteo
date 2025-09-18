# Hidrobart Costeo
# frontend/pages/p_imp_provData.py

from nicegui import ui
import pandas as pd
import io
from services.db_services import insertar_proveedor


@ui.page("/importar_proveedores")
def importar_proveedores():
    ui.label("Importar Proveedores desde CSV/Excel").classes("text-2xl font-bold mb-4")

    def handle_upload(e):
        try:
            # Leer archivo subido en memoria
            file_bytes = e.content.read()

            # Detectar tipo (CSV o Excel)
            if e.name.endswith(".csv"):
                df = pd.read_csv(io.BytesIO(file_bytes))
            else:
                df = pd.read_excel(io.BytesIO(file_bytes))

            # Columnas requeridas según tu Excel
            required_cols = [
                "Proveedor",
                "Multiplicador",
                "Valor",
                "Flete de origen",
                "Arancel",
                "Gtos aduana",
                "Flete Mex",
                "Comentarios",
            ]

            # Validar que estén todas
            missing = [c for c in required_cols if c not in df.columns]
            if missing:
                ui.notify(
                    f"Error: faltan columnas requeridas en el archivo → {', '.join(missing)}",
                    color="negative",
                )
                return

            # Renombrar columnas Excel → BD
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

            # Insertar cada fila en la BD
            for _, row in df.iterrows():
                insertar_proveedor(row.to_dict())

            ui.notify(f"{len(df)} proveedores importados correctamente ✅")
        except Exception as ex:
            ui.notify(f"Error al importar: {ex}", color="negative")

    # Botón de upload
    ui.upload(
        on_upload=handle_upload,
        auto_upload=True,
        multiple=False,
        label="Subir archivo"
    ).classes("mb-4")
