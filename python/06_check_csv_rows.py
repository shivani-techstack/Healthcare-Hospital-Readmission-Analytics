
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
file_path = BASE_DIR / "outputs" / "healthcare_cleaned.csv"

# Read the CSV using the Python CSV parser
df = pd.read_csv(file_path, low_memory=False)

print("CSV data rows:", len(df))
print("Unique encounter IDs:", df["encounter_id"].nunique())
print("Unique patients:", df["patient_nbr"].nunique())
print("Duplicate rows:", df.duplicated().sum())

# Check the first and last encounter IDs
print("First encounter ID:", df["encounter_id"].iloc[0])
print("Last encounter ID:", df["encounter_id"].iloc[-1])
