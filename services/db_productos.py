# services/db_productos.py

from typing import Optional
import pandas as pd
from sqlalchemy import text
from core.db import engine


def get_productos_activos():
    query = """
    SELECT *
    FROM vw_prod_data_latest
    ORDER BY proveedor, familia, nombre;
    """
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df


def insertar_producto(row: dict):
    q = text("""
        INSERT INTO tbl_prod_data (
            prov_name, prov_famil, prod_sku_prov, prod_sku_sys,
            prod_name, prod_createby
        )
        VALUES (
            :prov_name, :prov_famil, :prod_sku_prov, :prod_sku_sys,
            :prod_name, :prod_createby
        )
        ON DUPLICATE KEY UPDATE
            prod_sku_sys    = VALUES(prod_sku_sys),
            prod_name       = VALUES(prod_name),
            prod_updateby   = VALUES(prod_createby),
            prod_updatedate = NOW();
    """)

    params = {
        "prov_name": row["prov_name"],
        "prov_famil": row["prov_famil"],
        "prod_sku_prov": row["prod_sku_prov"],
        "prod_sku_sys": row.get("prod_sku_sys", ""),
        "prod_name": row.get("prod_name", ""),
        "prod_createby": row.get("prod_createby", "Philippe"),
    }

    with engine.begin() as conn:
        conn.execute(q, params)


def get_productos_por_fecha(fecha: str) -> pd.DataFrame:
    query = text("""
        SELECT prod_id, prov_name, prov_famil, prod_sku_prov, prod_sku_sys,
               prod_name, prod_version,
               prod_createdate, prod_updatedate
        FROM tbl_prod_data
        WHERE DATE(prod_createdate) = :fecha
           OR DATE(prod_updatedate) = :fecha
        ORDER BY prod_id DESC
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn, params={"fecha": fecha})

    for col in ["prod_createdate", "prod_updatedate"]:
        if col in df.columns:
            df[col] = df[col].astype(str)

    return df


def get_precios(
    proveedor: Optional[str] = None,
    familia: Optional[str] = None,
    sku_prov: Optional[str] = None
) -> pd.DataFrame:
    """
    Llama al SP sp_get_precios y devuelve precios filtrados con alias amigables.
    """
    query = text("""
        CALL sp_get_precios(:p_proveedor, :p_familia, :p_sku_prov)
    """)

    with engine.connect() as conn:
        df = pd.read_sql(
            query,
            conn,
            params={
                "p_proveedor": proveedor or "",
                "p_familia": familia or "",
                "p_sku_prov": sku_prov or "",
            }
        )

    # Renombrar columnas a amigables directamente aquí
    df = df.rename(columns={
        "prov_name": "proveedor",
        "prov_famil": "familia",
        "prod_sku_prov": "sku_prov",
        "prod_price_prov": "precio",
        "price_version": "version",
        "price_vig_ini": "vigencia_inicio",
        "price_vig_fin": "vigencia_fin",
        "price_updatedate": "fecha_update",
        "price_updateby": "usuario_update",
    })

    return df
