
import pandas as pd

df = pd.read_csv("data/diabetic_data.csv")

print("Total rows:", len(df))

print(
    "Unique encounter IDs:",
    df["encounter_id"].nunique()
)

print(
    "Duplicate encounter IDs:",
    df["encounter_id"].duplicated().sum()
)

print(
    "Unique patients:",
    df["patient_nbr"].nunique()
)

print(
    "Patients with multiple encounters:",
    (df.groupby("patient_nbr")["encounter_id"].nunique() > 1).sum()
)
