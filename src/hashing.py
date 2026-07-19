import hashlib

def hash_identifier(df):

    df = df.copy()

    df["Hashed Identifier"] = df["Resale Identifier"].apply(
        lambda x: hashlib.sha256(
            x.encode("utf-8")
        ).hexdigest()
    )

    return df