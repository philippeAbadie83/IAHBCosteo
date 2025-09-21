# services/db_services.py

import pandas as pd
from sqlalchemy import text
from datetime import datetime

from core.db import engine, get_session  # usa solo los del core


def safe_percent(value):
    try:
        val = float(value)
        if 0 <= val <= 100:
            return round(val, 2)
        return 0.0
    except (ValueError, TypeError):
        return 0.0

def insertar_proveedor(row: dict):
    """
    UPSERT por (prov_name, prov_famil).
    Si no existe -> INSERT.
    Si existe    -> UPDATE (dispara el trigger BEFORE UPDATE para versionado e historial).
    """
    q = text("""
        INSERT INTO tbl_prov_data (
            prov_name, prov_famil, prov_multip,
            prov_pct_fleteorig, prov_pct_arancel, prov_pct_gtoaduana, prov_pct_fletedest,
            prov_coment, prov_createby
        )
        VALUES (
            :prov_name, :prov_famil, :prov_multip,
            :prov_pct_fleteorig, :prov_pct_arancel, :prov_pct_gtoaduana, :prov_pct_fletedest,
            :prov_coment, :prov_createby
        )
        ON DUPLICATE KEY UPDATE
            prov_multip        = VALUES(prov_multip),
            prov_pct_fleteorig = VALUES(prov_pct_fleteorig),
            prov_pct_arancel   = VALUES(prov_pct_arancel),
            prov_pct_gtoaduana = VALUES(prov_pct_gtoaduana),
            prov_pct_fletedest = VALUES(prov_pct_fletedest),
            prov_coment        = VALUES(prov_coment),
            prov_updateby      = VALUES(prov_createby),
            prov_updatedate    = NOW();
    """)

    params = {
        "prov_name": row["prov_name"],
        "prov_famil": row["prov_famil"],
        "prov_multip": float(row.get("prov_multip", 0) or 0),
        "prov_pct_fleteorig": safe_percent(row.get("prov_pct_fleteorig")),
        "prov_pct_arancel":   safe_percent(row.get("prov_pct_arancel")),
        "prov_pct_gtoaduana": safe_percent(row.get("prov_pct_gtoaduana")),
        "prov_pct_fletedest": safe_percent(row.get("prov_pct_fletedest")),
        "prov_coment": row.get("prov_coment", ""),
        "prov_createby": row.get("prov_createby", "Philippe"),
    }

    session = get_session()
    try:
        session.execute(q, params)
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def update_proveedor(prov_id: int, multip: float, flete: float, arancel: float,
                     gto_aduana: float, flete_dest: float, comentario: str, usuario: str):
    query = text("""
        UPDATE tbl_prov_data
        SET prov_multip = :prov_multip,
            prov_pct_fleteorig = :prov_pct_fleteorig,
            prov_pct_arancel = :prov_pct_arancel,
            prov_pct_gtoaduana = :prov_pct_gtoaduana,
            prov_pct_fletedest = :prov_pct_fletedest,
            prov_coment = :prov_coment,
            prov_updateby = :prov_updateby,
            prov_updatedate = NOW()
        WHERE prov_id = :prov_id
    """)
    session = get_session()
    try:
        session.execute(query, {
            "prov_id": prov_id,
            "prov_multip": float(multip or 0),
            "prov_pct_fleteorig": safe_percent(flete),
            "prov_pct_arancel": safe_percent(arancel),
            "prov_pct_gtoaduana": safe_percent(gto_aduana),
            "prov_pct_fletedest": safe_percent(flete_dest),
            "prov_coment": comentario or "",
            "prov_updateby": usuario,
        })
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()



def get_proveedores_activos():
    query = """
    SELECT
        prov_id AS id,
        prov_name AS proveedor,
        prov_famil AS familia,
        prov_multip AS valor,
        prov_pct_fleteorig AS flete_origen,
        prov_pct_arancel AS arancel,
        prov_pct_gtoaduana AS gtos_aduana,
        prov_pct_fletedest AS flete_mex,
        prov_pct_totgto AS total_gastos,
        prov_coment AS comentarios,
        prov_version AS version,
        prov_updatedate AS fecha_update,
        prov_updateby AS usuario_update
    FROM vw_prov_data_latest;
    """
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df

def get_proveedores_por_fecha(fecha: str) -> pd.DataFrame:
    """
    Devuelve proveedores creados o actualizados en una fecha específica (YYYY-MM-DD).
    """
    query = text("""
        SELECT prov_id, prov_name, prov_famil, prov_multip,
               prov_pct_fleteorig, prov_pct_arancel,
               prov_pct_gtoaduana, prov_pct_fletedest,
               prov_coment, prov_version,
               prov_createdate, prov_updatedate
        FROM tbl_prov_data
        WHERE DATE(prov_createdate) = :fecha
           OR DATE(prov_updatedate) = :fecha
        ORDER BY prov_id DESC
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn, params={"fecha": fecha})
    return df

