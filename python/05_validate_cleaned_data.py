
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
file_path = BASE_DIR / "outputs" / "healthcare_cleaned.csv"

df = pd.read_csv(file_path,low_memory=False)

print("CLEANED DATA VALIDATION")
print("-" * 35)

# 1. Check dimensions
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Check duplicate rows
print("Duplicate rows:", df.duplicated().sum())

# 3. Check unique identifiers
print("Unique encounters:", df["encounter_id"].nunique())
print("Unique patients:", df["patient_nbr"].nunique())

# 4. Check readmission counts
print("\nReadmission categories:")
print(df["readmitted"].value_counts())

print("\n30-day readmission indicator:")
print(df["readmitted_30d"].value_counts())

# 5. Check whether '?' remains
print(
    "\nRemaining '?' values:",
    df.astype("string").eq("?").sum().sum()
)

print("\nValidation completed.")
