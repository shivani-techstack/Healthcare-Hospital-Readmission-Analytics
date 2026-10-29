
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
file_path = BASE_DIR / "outputs" / "healthcare_cleaned.csv"

df = pd.read_csv(file_path, low_memory=False)

# Identify columns that are completely empty
blank_columns = []

for col in df.columns:
    values = df[col].astype("string").str.strip()
    empty_count = (values.isna() | values.eq("")).sum()

    if empty_count == len(df):
        blank_columns.append(col)

print("Dataset shape:", df.shape)
print("\nCompletely blank columns:")

if blank_columns:
    for col in blank_columns:
        print(col)
else:
    print("No completely blank columns found.")

print("\nMissing values by column:")
print(df.isna().sum()[df.isna().sum() > 0].sort_values(ascending=False))
