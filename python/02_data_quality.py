
import pandas as pd

# Load the original dataset
df = pd.read_csv("data/diabetic_data.csv")

# Convert '?' placeholders into proper missing values
df = df.replace("?", pd.NA)

# Calculate missing values for every column
missing_count = df.isna().sum()

# Calculate missing percentage for every column
missing_percentage = (missing_count / len(df)) * 100

# Create a summary table
quality_report = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage": missing_percentage.round(2)
})

# Show columns with missing values, highest first
quality_report = quality_report[
    quality_report["Missing_Count"] > 0
].sort_values("Missing_Percentage", ascending=False)

print("DATA QUALITY REPORT")
print(quality_report)

# Save the report for project documentation
quality_report.to_csv("outputs/data_quality_report.csv")

print("\nReport saved successfully!")
