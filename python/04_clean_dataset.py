
import pandas as pd
import numpy as np
from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parents[1]

# Load original data
input_path = BASE_DIR / "data" / "diabetic_data.csv"
output_dir = BASE_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

df = pd.read_csv(input_path)

print("Original shape:", df.shape)

# Step 1: Convert '?' placeholders to proper missing values
df = df.replace("?", np.nan)

# Step 2: Create a 30-day readmission indicator
# 1 = readmitted within 30 days
# 0 = not readmitted within 30 days
df["readmitted_30d"] = np.where(
    df["readmitted"] == "<30", 1, 0
)

# Step 3: Validate the changes
print("\nCleaned shape:", df.shape)

print("\nMissing values in selected columns:")
print(
    df[["weight", "medical_specialty", "payer_code"]]
    .isna()
    .sum()
)

print("\nReadmission indicator:")
print(df["readmitted_30d"].value_counts())

# Step 4: Save a separate working dataset
output_path = output_dir / "healthcare_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nSaved cleaned dataset to:", output_path)
print("Original dataset remains unchanged.")
