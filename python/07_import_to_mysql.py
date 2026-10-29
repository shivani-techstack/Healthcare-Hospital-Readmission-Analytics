
import csv
import mysql.connector
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CSV_PATH = BASE_DIR / "outputs" / "healthcare_cleaned.csv"

# Enter the same connection details you use in MySQL Workbench.
# Keep your password private.
config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",       # Change if your MySQL username differs
    "password": "shivani2729",
    "database": "healthcare_analytics",
}

conn = None
cursor = None

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Create a separate table with the same columns as the CSV.
    # Use TEXT for flexible source values during this initial import.
    with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        headers = next(reader)

    column_definitions = []
    for column in headers:
        safe_name = column.replace("`", "``")
        if column == "encounter_id" or column == "patient_nbr":
            column_definitions.append(f"`{safe_name}` BIGINT")
        elif column == "readmitted_30d":
            column_definitions.append(f"`{safe_name}` TINYINT")
        else:
            column_definitions.append(f"`{safe_name}` TEXT")

    cursor.execute("DROP TABLE IF EXISTS diabetic_data_final")
    cursor.execute(
        "CREATE TABLE diabetic_data_final ("
        + ", ".join(column_definitions)
        + ")"
    )
    conn.commit()

    columns_sql = ", ".join(f"`{c.replace('`', '``')}`" for c in headers)
    placeholders = ", ".join(["%s"] * len(headers))
    insert_sql = (
        f"INSERT INTO diabetic_data_final ({columns_sql}) "
        f"VALUES ({placeholders})"
    )

    batch_size = 1000
    batch = []
    inserted = 0

    with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            values = []
            for column in headers:
                value = row[column]
                if value == "":
                    value = None
                elif column in ("encounter_id", "patient_nbr", "readmitted_30d"):
                    value = int(value)
                values.append(value)

            batch.append(tuple(values))

            if len(batch) >= batch_size:
                cursor.executemany(insert_sql, batch)
                conn.commit()
                inserted += len(batch)
                batch.clear()
                print(f"Inserted {inserted} rows...")

        if batch:
            cursor.executemany(insert_sql, batch)
            conn.commit()
            inserted += len(batch)

    cursor.execute("SELECT COUNT(*) FROM diabetic_data_final")
    actual_count = cursor.fetchone()[0]

    print("\nImport finished.")
    print("Rows submitted:", inserted)
    print("Rows in MySQL:", actual_count)

    if actual_count == 101766:
        print("SUCCESS: All expected rows are present.")
    else:
        print("WARNING: Row count differs from expected 101766.")

except mysql.connector.Error as error:
    if conn:
        conn.rollback()
    print("MySQL error:", error)

except Exception as error:
    if conn:
        conn.rollback()
    print("Import error:", error)

finally:
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
