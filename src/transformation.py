import pandas as pd
import re


def create_resale_identifier(df):

    df = df.copy()

    # Remove previously created columns if they exist
    for col in ["avg_price", "Resale Identifier"]:
        if col in df.columns:
            df = df.drop(columns=[col])

    # Calculate average resale price
    avg_price = (
        df.groupby(
            ["month", "town", "flat_type"]
        )["resale_price"]
        .mean()
        .reset_index(name="avg_price")
    )

    # Merge average price back
    df = df.merge(
        avg_price,
        on=["month", "town", "flat_type"],
        how="left"
    )

    # Create Resale Identifier
    def build_identifier(row):

        # Remove non-numeric characters from block
        block_digits = re.sub(r"\D", "", str(row["block"]))

        # First 3 digits, padded with zeros if required
        block_digits = block_digits[:3].zfill(3)

        # First two digits of average resale price
        avg_digits = str(int(row["avg_price"]))[:2]

        # Month
        month = row["month"][-2:]

        # First character of town
        town_initial = row["town"][0]

        return f"S{block_digits}{avg_digits}{month}{town_initial}"

    df["Resale Identifier"] = df.apply(
        build_identifier,
        axis=1
    )

    return df