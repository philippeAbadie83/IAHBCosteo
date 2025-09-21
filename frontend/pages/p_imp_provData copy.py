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
from services.db_services import insertar_proveedor
from core import layout


@ui.page("/importar_proveedores")
def importar_proveedores():
    """Página para importar proveedores desde archivo CSV o Excel."""

    def content():
        # ----------------- Título -----------------
        ui.label("Importar Proveedores desde CSV/Excel") \
            .classes("text-2xl font-bold mb-6")

        # ----------------- Handler de Upload -----------------
        def handle_upload(e):
            try:
                # 1. Leer archivo subido en memoria
                file_bytes = e.content.read()

                # 2. Detectar tipo: CSV o Excel
                if e.name.endswith(".csv"):
                    df = pd.read_csv(io.BytesIO(file_bytes))
                else:
                    df = pd.read_excel(io.BytesIO(file_bytes))

                # 3. Definir columnas requeridas (según el Excel base)
                required_cols = [
                    "Proveedor",
                    "Multiplicador",      # Se usa como prov_famil
                    "Valor",              # Se usa como prov_multip
                    "Flete de orígen",    # Exactamente igual al Excel
                    "Arancel",
                    "Gtos aduana",
                    "Flete Mex",
                    "Comentarios",
                ]

                # 4. Validar columnas → notificar si falta alguna
                missing = [c for c in required_cols if c not in df.columns]
                if missing:
                    ui.notify(
                        f"Error: faltan columnas en el archivo → {', '.join(missing)}",
                        color="negative",
                    )
                    return

                # 5. Renombrar columnas Excel → campos BD
                df = df.rename(columns={
                    "Proveedor": "prov_name",
                    "Multiplicador": "prov_famil",       # Familia
                    "Valor": "prov_multip",              # Multip (SQL)
                    "Flete de orígen": "prov_pct_fleteorig",
                    "Arancel": "prov_pct_arancel",
                    "Gtos aduana": "prov_pct_gtoaduana",
                    "Flete Mex": "prov_pct_fletedest",
                    "Comentarios": "prov_coment",
                })

                # 6. Reemplazar NaN por valores válidos
                df = df.fillna({
                    "prov_coment": "",
                    "prov_multip": 0,
                    "prov_pct_fleteorig": 0,
                    "prov_pct_arancel": 0,
                    "prov_pct_gtoaduana": 0,
                    "prov_pct_fletedest": 0,
                })

                # 7. Insertar cada fila en la BD con autor fijo
                for _, row in df.iterrows():
                    data = row.to_dict()
                    data["prov_createby"] = "Philippe Abadie"
                    insertar_proveedor(data)

                ui.notify(f"{len(df)} proveedores importados correctamente ✅")

            except Exception as ex:
                # Mostrar error en la UI si ocurre
                ui.notify(f"Error al importar: {ex}", color="negative")

        # ----------------- Botón Upload -----------------
        ui.upload(
            on_upload=handle_upload,
            auto_upload=True,
            multiple=False,
            label="Subir archivo"
        ).classes("mb-4")

    # Integrar en el layout general
    layout.render(content)
