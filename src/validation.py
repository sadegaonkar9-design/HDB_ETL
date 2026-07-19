import pandas as pd
import re


def validate_dataset(df):

    clean_df = df.copy()

    failed_records = []


    # =====================================
    # Rule 1: Month Validation
    # =====================================

    month_pattern = r"^\d{4}-\d{2}$"


    invalid_month = (
        ~clean_df["month"]
        .astype(str)
        .str.match(month_pattern)
    )


    failed_records.append(
        clean_df[invalid_month]
        .assign(
            failed_reason="Invalid month format"
        )
    )


    clean_df = clean_df[
        ~invalid_month
    ]


    # =====================================
    # Rule 2: Town Validation
    # =====================================

    valid_towns = (
        df["town"]
        .dropna()
        .unique()
    )


    invalid_town = (
        ~clean_df["town"]
        .isin(valid_towns)
    )


    failed_records.append(
        clean_df[invalid_town]
        .assign(
            failed_reason="Invalid town"
        )
    )


    clean_df = clean_df[
        ~invalid_town
    ]


    # =====================================
    # Rule 3: Flat Type Validation
    # =====================================

    valid_flat_types = [
        "1 ROOM",
        "2 ROOM",
        "3 ROOM",
        "4 ROOM",
        "5 ROOM",
        "EXECUTIVE",
        "MULTI GENERATION",
        "MULTI-GENERATION"
    ]


    invalid_flat_type = (
        ~clean_df["flat_type"]
        .isin(valid_flat_types)
    )


    failed_records.append(
        clean_df[invalid_flat_type]
        .assign(
            failed_reason="Invalid flat type"
        )
    )


    clean_df = clean_df[
        ~invalid_flat_type
    ]


    # =====================================
    # Rule 4: Storey Range Validation
    # =====================================

    storey_pattern = r"^\d{2} TO \d{2}$"


    invalid_storey = (
        ~clean_df["storey_range"]
        .astype(str)
        .str.match(storey_pattern)
    )


    failed_records.append(
        clean_df[invalid_storey]
        .assign(
            failed_reason="Invalid storey range"
        )
    )


    clean_df = clean_df[
        ~invalid_storey
    ]


    # =====================================
    # Rule 5: Floor Area Validation
    # =====================================

    invalid_area = (
        (clean_df["floor_area_sqm"] <= 0)
        |
        (clean_df["floor_area_sqm"] > 500)
    )


    failed_records.append(
        clean_df[invalid_area]
        .assign(
            failed_reason="Invalid floor area"
        )
    )


    clean_df = clean_df[
        ~invalid_area
    ]


    # =====================================
    # Rule 6: Resale Price Validation
    # =====================================

    invalid_price = (
        clean_df["resale_price"] <= 0
    )


    failed_records.append(
        clean_df[invalid_price]
        .assign(
            failed_reason="Invalid resale price"
        )
    )


    clean_df = clean_df[
        ~invalid_price
    ]


    # =====================================
    # Combine failed records
    # =====================================

    failed_df = pd.concat(
        failed_records,
        ignore_index=True
    )


    failed_df = (
        failed_df
        .drop_duplicates()
    )


    return clean_df, failed_df