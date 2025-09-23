
# utils/helpers.py - PRIMERO ACTUALIZAR ESTE ARCHIVO

import pandas as pd
import numpy as np
from decimal import Decimal
from typing import Optional, List  # 👈 Agregar esto

def sanitize_dataframe(df: pd.DataFrame, percent_columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Convierte un DataFrame a un formato seguro para serialización JSON.
    """
    if df is None or df.empty:
        return df

    df = df.copy()

    # 🔹 Fechas → string
    for col in df.select_dtypes(include=[np.datetime64]).columns:
        df[col] = df[col].dt.strftime("%Y-%m-%d %H:%M:%S")

    # 🔹 Decimals → float
    for col in df.columns:
        df[col] = df[col].apply(lambda x: float(x) if isinstance(x, Decimal) else x)

    # 🔹 PORCENTAJES → string con formato (NUEVO)
    if percent_columns:
        for col in percent_columns:
            if col in df.columns:
                df[col] = df[col].apply(_format_percent)

    return df

def _format_percent(value):
    """Formatea valores decimales como porcentajes"""
    if value is None or pd.isna(value):
        return "0%"

    try:
        # Si es string que ya tiene %, dejarlo igual
        if isinstance(value, str) and '%' in value:
            return value

        # Convertir a float
        num = float(value)

        # Si está entre 0 y 1, convertirlo a porcentaje (0.05 → 5%)
        if 0 <= num <= 1:
            num = num * 100

        return f"{round(num)}%"

    except (ValueError, TypeError):
        return str(value)
