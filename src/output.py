import os


def save_outputs(
    master_df,
    clean_df,
    transformed_df,
    hashed_df,
    failed_df,
    duplicate_df,
    anomaly_df
):

    folders = [
        "output/raw",
        "output/cleaned",
        "output/transformed",
        "output/hashed",
        "output/failed"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    master_df.to_csv(
        "output/raw/master_dataset.csv",
        index=False
    )

    clean_df.to_csv(
        "output/cleaned/cleaned_dataset.csv",
        index=False
    )

    transformed_df.to_csv(
        "output/transformed/transformed_dataset.csv",
        index=False
    )

    hashed_df.to_csv(
        "output/hashed/hashed_dataset.csv",
        index=False
    )

    failed_df.to_csv(
        "output/failed/validation_failed.csv",
        index=False
    )

    duplicate_df.to_csv(
        "output/failed/duplicate_records.csv",
        index=False
    )

    anomaly_df.to_csv(
        "output/failed/anomaly_records.csv",
        index=False
    )

    print("Output files generated successfully.")