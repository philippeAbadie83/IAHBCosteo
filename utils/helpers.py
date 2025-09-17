# utils/helpers.py

import pandas as pd
import numpy as np
from decimal import Decimal


def sanitize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convierte un DataFrame a un formato seguro para serialización JSON:
    - Datetime -> string con formato YYYY-MM-DD HH:MM:SS
    - Decimal -> float
    - Otros tipos se dejan tal cual
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

    return df
