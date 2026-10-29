# Starter DAX measures

Assume your imported table is named `diabetic_data`. Adjust names to match your model.

```DAX
Total Encounters =
COUNTROWS(diabetic_data)

Unique Patients =
DISTINCTCOUNT(diabetic_data[patient_nbr])

Readmitted Within 30 Days =
CALCULATE(
    [Total Encounters],
    diabetic_data[readmitted] = "<30"
)

30-Day Readmission Rate =
DIVIDE(
    [Readmitted Within 30 Days],
    [Total Encounters],
    0
)

Average Length of Stay =
AVERAGE(diabetic_data[time_in_hospital])

Average Medication Count =
AVERAGE(diabetic_data[num_medications])

Average Prior Inpatient Visits =
AVERAGE(diabetic_data[number_inpatient])

Encounters Not Readmitted Within 30 Days =
CALCULATE(
    [Total Encounters],
    diabetic_data[readmitted] IN {">30", "NO"}
)
```

Format `30-Day Readmission Rate` as Percentage. Validate the measure against a SQL result.

Caution: the source is encounter-level, so `Total Encounters` and `Unique Patients` are different metrics. The 30-day readmission rate above uses all encounters as the denominator; document that definition and use it consistently.
