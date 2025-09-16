# services/db_services.py

import pandas as pd
from sqlalchemy import text
from core.db import engine

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
