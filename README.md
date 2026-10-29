# Hospital Insights 360° — Healthcare Data Analyst Project

## Project overview
Analyze hospital encounters for patients with diabetes to understand readmission patterns, length of stay, admission categories, diagnoses, and data quality.

**Dataset:** UCI Machine Learning Repository — Diabetes 130-US Hospitals for Years 1999–2008  
**Official source:** https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008  
**Scale:** 101,766 encounters, 47 features, 130 US hospitals (1999–2008).  
**Tools:** Python, Pandas, NumPy, Matplotlib, SQL, Power BI, DAX.

> This is historical US hospital data. Do not present it as current Indian hospital performance. This project is for educational and portfolio analysis, not medical decision-making.

## Business questions
1. What is the total number of encounters and unique patients?
2. What percentage of encounters resulted in readmission within 30 days?
3. How does length of stay vary by admission type?
4. Which diagnosis groups account for the most encounters?
5. Are prior inpatient, emergency, and outpatient visits associated with readmission?
6. How do medication counts vary by readmission status?
7. Which columns have missing, unknown, or inconsistent values?

## Repository structure
```text
healthcare-hospital-analytics/
├── data/
│   └── README.md
├── python/
│   └── 01_eda_starter.py
├── sql/
│   └── 01_business_questions.sql
├── powerbi/
│   ├── dax_measures.md
│   └── dashboard_build_guide.md
└── README.md
```

## Setup
1. Download `diabetic_data.csv` and `IDS_mapping.csv` from the official UCI page.
2. Put the files in the `data/` folder (do not commit patient-level data to a public repository).
3. Install packages:
   ```bash
   pip install pandas numpy matplotlib
   ```
4. Run:
   ```bash
   python python/01_eda_starter.py
   ```
5. Load a cleaned CSV into your SQL database, then adapt and run the SQL questions.
6. Import the cleaned dataset into Power BI and follow `powerbi/dashboard_build_guide.md`.

## Suggested project phases
- Phase 1: Understand the data dictionary and profile data quality.
- Phase 2: Define cleaning decisions and document every change.
- Phase 3: Analyze business questions in Python and SQL.
- Phase 4: Build a three-page Power BI report: Overview, Readmissions, Patient & Care Patterns.
- Phase 5: Write evidence-based insights and limitations.

## Important data notes
- `readmitted` has values `<30`, `>30`, and `NO`. Define the 30-day readmission measure explicitly as `<30`.
- Several fields use `?` to represent unknown/missing values.
- `encounter_id` identifies an encounter; `patient_nbr` identifies a patient. One patient can have multiple encounters.
- Do not claim causation from descriptive associations.
- Use the UCI dataset citation and license information on your project page.
