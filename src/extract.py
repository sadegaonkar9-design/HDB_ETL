import pandas as pd
import glob
import os


def extract_data(raw_path):

    csv_files = glob.glob(
        os.path.join(raw_path, "*.csv")
    )

    if not csv_files:
        raise Exception(
            "No CSV files found"
        )


    datasets = []


    for file in csv_files:

        print(
            f"Reading file: {file}"
        )

        df = pd.read_csv(file)


        # Data lineage
        df["source_file"] = os.path.basename(file)


        datasets.append(df)



    master_df = pd.concat(
        datasets,
        ignore_index=True,
        sort=False
    )


    return master_df