import pandas as pd
from datetime import datetime


# =====================================
# Standardize Flat Model
# =====================================

def standardize_flat_model(df):

    df = df.copy()

    df["flat_model"] = (
        df["flat_model"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    replacements = {
        "MULTI GENERATION": "MULTI-GENERATION",
        "2-ROOM": "2 ROOM",
        "3-ROOM": "3 ROOM",
        "4-ROOM": "4 ROOM",
        "5-ROOM": "5 ROOM"
    }

    df["flat_model"] = df["flat_model"].replace(replacements)

    return df


# =====================================
# Remove Duplicate Records
# =====================================

def remove_duplicates(df):

    df = df.copy()

    key_columns = [
        c for c in df.columns
        if c != "resale_price"
    ]

    df = df.sort_values(
        by="resale_price",
        ascending=False
    )

    duplicate_mask = df.duplicated(
        subset=key_columns,
        keep="first"
    )

    duplicate_df = df.loc[duplicate_mask].copy()

    duplicate_df["failed_reason"] = (
        "Duplicate record - Lower resale price"
    )

    clean_df = df.loc[~duplicate_mask].copy()

    return clean_df, duplicate_df


# =====================================
# Remaining Lease Calculation
# =====================================

def calculate_remaining_lease(df):

    df = df.copy()

    today = datetime.today()

    expiry_year = (
        df["lease_commence_date"] + 99
    )

    remaining_months = (
        (expiry_year - today.year) * 12
        - (today.month - 1)
    )

    remaining_months = remaining_months.clip(lower=0)

    df["remaining_lease"] = (
        (remaining_months // 12)
        .astype(int)
        .astype(str)
        + " years "
        + (remaining_months % 12)
        .astype(int)
        .astype(str)
        + " months"
    )

    return df


# =====================================
# Detect Price Anomalies (IQR Method)
# =====================================

def detect_price_anomalies(df):

    df = df.copy()

    q1 = df["resale_price"].quantile(0.25)
    q3 = df["resale_price"].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - (1.5 * iqr)
    upper = q3 + (1.5 * iqr)

    df["is_price_anomaly"] = (
        (df["resale_price"] < lower)
        |
        (df["resale_price"] > upper)
    )

    anomaly_df = df[
        df["is_price_anomaly"]
    ].copy()

    anomaly_df["failed_reason"] = (
        "Potential resale price anomaly"
    )

    return df, anomaly_df