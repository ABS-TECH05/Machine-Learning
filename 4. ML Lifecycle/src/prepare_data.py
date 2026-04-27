import argparse
import os
import pandas as pd


def clean_classes(value):
    text = str(value).strip().lower()
    return 1 if text == "fire" else 0


def prepare(input_path: str, output_path: str) -> None:
    df = pd.read_csv(input_path)

    # Clean column names and class labels
    df.columns = [col.strip() for col in df.columns]
    df["Classes"] = df["Classes"].apply(clean_classes)

    # Convert all columns to numeric after encoding Classes
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna().reset_index(drop=True)

    # Keep the same features used by the Flask form
    keep_columns = [
        "Temperature", "RH", "Ws", "Rain", "FFMC",
        "DMC", "ISI", "Classes", "Region", "FWI"
    ]
    df = df[keep_columns]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved processed data to {output_path}. Shape: {df.shape}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw/Algerian_forest_fires_cleaned_dataset.csv")
    parser.add_argument("--output", default="data/processed/forest_fire_processed.csv")
    args = parser.parse_args()
    prepare(args.input, args.output)
