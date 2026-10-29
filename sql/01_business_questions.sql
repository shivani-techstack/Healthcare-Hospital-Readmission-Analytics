/*
Starter SQL for a table named diabetic_data.
Import your cleaned CSV into your SQL database first.
SQL syntax is broadly MySQL-compatible; adjust date/functions for your DBMS if needed.
*/

-- 1. Total encounters and unique patients
SELECT
    COUNT(*) AS total_encounters,
    COUNT(DISTINCT patient_nbr) AS unique_patients
FROM diabetic_data;

-- 2. Readmission category distribution
SELECT
    readmitted,
    COUNT(*) AS encounters,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM diabetic_data), 2) AS pct_of_encounters
FROM diabetic_data
GROUP BY readmitted
ORDER BY encounters DESC;

-- 3. 30-day readmission rate (readmitted = '<30')
SELECT
    SUM(CASE WHEN readmitted = '<30' THEN 1 ELSE 0 END) AS readmitted_within_30_days,
    COUNT(*) AS total_encounters,
    ROUND(
        100.0 * SUM(CASE WHEN readmitted = '<30' THEN 1 ELSE 0 END) / NULLIF(COUNT(*), 0),
        2
    ) AS readmission_30d_pct
FROM diabetic_data;

-- 4. Average length of stay by admission type
SELECT
    admission_type_id,
    COUNT(*) AS encounters,
    ROUND(AVG(time_in_hospital), 2) AS avg_length_of_stay
FROM diabetic_data
GROUP BY admission_type_id
ORDER BY avg_length_of_stay DESC;

-- 5. Prior inpatient visits vs readmission category
SELECT
    number_inpatient,
    readmitted,
    COUNT(*) AS encounters
FROM diabetic_data
GROUP BY number_inpatient, readmitted
ORDER BY number_inpatient, readmitted;

-- 6. Medication count by readmission category
SELECT
    readmitted,
    ROUND(AVG(num_medications), 2) AS avg_medications,
    COUNT(*) AS encounters
FROM diabetic_data
GROUP BY readmitted
ORDER BY avg_medications DESC;

-- 7. Encounters by medical specialty (unknown values should be handled during cleaning)
SELECT
    medical_specialty,
    COUNT(*) AS encounters
FROM diabetic_data
GROUP BY medical_specialty
ORDER BY encounters DESC
LIMIT 10;

-- 8. Rank readmission categories by encounter volume
WITH readmission_counts AS (
    SELECT readmitted, COUNT(*) AS encounter_count
    FROM diabetic_data
    GROUP BY readmitted
)
SELECT
    readmitted,
    encounter_count,
    DENSE_RANK() OVER (ORDER BY encounter_count DESC) AS volume_rank
FROM readmission_counts;

-- 9. Data quality: count unknown markers before replacing '?' with NULL
-- Run against the original imported table if '?' placeholders were preserved.
SELECT
    SUM(CASE WHEN race = '?' THEN 1 ELSE 0 END) AS unknown_race,
    SUM(CASE WHEN gender = 'Unknown/Invalid' THEN 1 ELSE 0 END) AS unknown_gender,
    SUM(CASE WHEN medical_specialty = '?' THEN 1 ELSE 0 END) AS unknown_specialty
FROM diabetic_data;
