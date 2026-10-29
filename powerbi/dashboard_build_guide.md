# Power BI dashboard build guide

## Page 1 — Hospital Overview
**KPI cards**
- Total Encounters
- Unique Patients
- 30-Day Readmission Rate
- Average Length of Stay

**Visuals**
- Bar chart: encounter count by readmission category
- Bar chart: encounters by admission type
- Column chart: average length of stay by admission type
- Slicers: gender, age group, admission type, readmission category

## Page 2 — Readmission Analysis
**Visuals**
- 100% stacked bar: readmission category by admission type
- Bar chart: readmission category by number of prior inpatient visits
- Column chart: average medication count by readmission category
- Matrix: prior inpatient visits and readmission category

**Interpretation rule:** describe patterns as associations, not causes. The data does not prove that a particular factor causes readmission.

## Page 3 — Patient & Care Patterns
**Visuals**
- Encounters by age group
- Encounters by diagnosis group (use the provided diagnosis fields carefully)
- Average length of stay by diagnosis group
- Encounters by medical specialty
- Data quality card/table showing unknown values

## Design recommendations
- Use a consistent two- or three-color palette and readable labels.
- Put the most important KPIs at the top.
- Use descriptive titles that state the question answered.
- Add tooltips and slicers only when they help answer a business question.
- Include a note: "Historical US dataset (1999–2008); descriptive analysis only."

## Before publishing
1. Validate each KPI against SQL.
2. Check whether `?` values and `Unknown/Invalid` categories were handled consistently.
3. Confirm that the readmission denominator is documented.
4. Avoid exposing patient-level data in public screenshots or reports.
5. Write 3–5 findings only after calculating them from the data.
