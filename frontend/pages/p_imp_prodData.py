# frontend/pages/p_imp_prodData.py -productos
from nicegui import ui
import pandas as pd
import io
from datetime import date
from services.db_productos import insertar_producto, get_productos_por_fecha
from core import layout
from frontend.components.tbl_base import crear_tabla


@ui.page("/p_imp_prodData")
def p_imp_prodData_page():
    """Página para importar productos desde archivo CSV o Excel."""

    def content():
        ui.label("Alta Productos desde CSV/Excel") \
            .classes("text-2xl font-bold mb-6")

        # ----------------- Handler Upload -----------------
        def handle_upload(e):
            try:
                file_bytes = e.content.read()

                if e.name.endswith(".csv"):
                    df = pd.read_csv(io.BytesIO(file_bytes))
                else:
                    df = pd.read_excel(io.BytesIO(file_bytes))

                # Columnas requeridas
                required_cols = [
                    "Proveedor", "Familia",
                    "No. part Prov", "Código del producto (en sistema)",
                    "Nombre del producto"
                ]
                missing = [c for c in required_cols if c not in df.columns]
                if missing:
                    ui.notify(f"Error: faltan columnas → {', '.join(missing)}",
                              color="negative")
                    return

                # Renombrar columnas → BD
                df = df.rename(columns={
                    "Proveedor": "prov_name",
                    "Familia": "prov_famil",
                    "No. part Prov": "prod_sku_prov",
                    "Código del producto (en sistema)": "prod_sku_sys",
                    "Nombre del producto": "prod_name",
                })

                df = df.fillna({
                    "prod_sku_sys": "",
                    "prod_name": "",
                })

                for _, row in df.iterrows():
                    data = row.to_dict()
                    data["prod_createby"] = "Philippe"
                    insertar_producto(data)

                ui.notify(f"{len(df)} productos importados correctamente ✅")

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
        df = get_productos_por_fecha(hoy)

        ui.label(f"Productos importados o actualizados el {hoy}") \
            .classes("text-xl font-bold mt-6 mb-4")

        if df.empty:
            ui.label("No hay registros importados/actualizados en la fecha").classes("text-gray-500")
        else:
            columnas = [
                {"name": "prov_name", "label": "Proveedor", "field": "prov_name"},
                {"name": "prov_famil", "label": "Familia", "field": "prov_famil"},
                {"name": "prod_sku_prov", "label": "SKU Proveedor", "field": "prod_sku_prov"},
                {"name": "prod_sku_sys", "label": "SKU Sistema", "field": "prod_sku_sys"},
                {"name": "prod_name", "label": "Nombre Producto", "field": "prod_name"},
                {"name": "prod_version", "label": "Versión", "field": "prod_version"},
                {"name": "prod_createdate", "label": "Creado", "field": "prod_createdate"},
                {"name": "prod_updatedate", "label": "Actualizado", "field": "prod_updatedate"},
            ]

            crear_tabla(
                nombre="Productos importados",
                columnas=columnas,
                data=df,
                exportar=True,
                congelar=["prov_name", "prov_famil", "prod_sku_prov"]
            )

    layout.render(content)
