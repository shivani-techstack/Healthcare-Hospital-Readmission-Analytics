"""Beginner-friendly EDA starter for the UCI diabetes hospital encounters dataset."""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "diabetic_data.csv"
OUT_DIR = ROOT / "outputs"
OUT_DIR.mkdir(exist_ok=True)

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Could not find {DATA_PATH}. Download diabetic_data.csv from the official UCI page "
        "and place it inside the project's data/ folder."
    )

df = pd.read_csv(DATA_PATH)

print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nMissing values (including '?' placeholders):")
print(df.isin(["?"]).sum().sort_values(ascending=False).head(15))
print("\nExact duplicate rows:", df.duplicated().sum())
print("\nUnique encounters:", df["encounter_id"].nunique())
print("Unique patients:", df["patient_nbr"].nunique())

# Standardize the dataset's '?' placeholder as missing.
df = df.replace("?", np.nan)

# Convert selected numeric fields safely.
numeric_cols = [
    "time_in_hospital", "num_lab_procedures", "num_procedures",
    "num_medications", "number_outpatient", "number_emergency",
    "number_inpatient", "number_diagnoses"
]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Readmission outcome: keep all three original categories and add a clear 30-day flag.
df["readmitted_30d"] = np.where(df["readmitted"].eq("<30"), 1,
                                np.where(df["readmitted"].isin([">30", "NO"]), 0, np.nan))

print("\nReadmission category counts:")
print(df["readmitted"].value_counts(dropna=False))
print("\n30-day readmission rate (% of encounters with known target):")
print(round(df["readmitted_30d"].mean() * 100, 2))

print("\nAverage length of stay by readmission category:")
print(df.groupby("readmitted", dropna=False)["time_in_hospital"].mean().round(2))

# Simple chart: encounters by readmission category.
df["readmitted"].value_counts(dropna=False).plot(kind="bar")
plt.title("Hospital Encounters by Readmission Category")
plt.xlabel("Readmission category")
plt.ylabel("Number of encounters")
plt.tight_layout()
plt.savefig(OUT_DIR / "encounters_by_readmission.png", dpi=150)
plt.close()

# Export a cleaned working file for SQL/Power BI. Review privacy and data minimization
# before sharing any exported data publicly.
df.to_csv(OUT_DIR / "diabetic_data_working_clean.csv", index=False)
print(f"\nSaved working file and chart in: {OUT_DIR}")
print("Next: document cleaning decisions and validate key metrics before dashboarding.")
