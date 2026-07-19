import pandas as pd


def profile_dataset(df):

    profile = {}

    # Dataset size
    profile["row_count"] = df.shape[0]

    profile["column_count"] = df.shape[1]


    # Column information

    profile["columns"] = list(df.columns)


    # Data types

    profile["data_types"] = (
        df.dtypes
        .astype(str)
        .to_dict()
    )


    # Missing values

    profile["missing_values"] = (
        df.isnull()
        .sum()
        .sort_values(
            ascending=False
        )
        .to_dict()
    )


    # Unique values

    profile["unique_count"] = (
        df.nunique()
        .to_dict()
    )


    # Duplicate rows

    profile["duplicate_records"] = (
        df.duplicated()
        .sum()
    )


    # Numerical statistics

    profile["statistics"] = (
        df.describe()
        .to_dict()
    )


    return profile