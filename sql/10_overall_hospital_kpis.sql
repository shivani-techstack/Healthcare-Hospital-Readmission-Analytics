
USE healthcare_analytics;

SELECT
    COUNT(*) AS total_encounters,

    COUNT(DISTINCT patient_nbr) AS unique_patients,

    SUM(
        CASE WHEN readmitted = '<30'
             THEN 1 ELSE 0 END
    ) AS readmissions_within_30_days,

    ROUND(
        100.0 * SUM(
            CASE WHEN readmitted = '<30'
                 THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS readmission_rate_pct,

    ROUND(AVG(time_in_hospital), 2)
        AS average_length_of_stay,

    ROUND(AVG(num_medications), 2)
        AS average_medications_per_encounter

FROM diabetic_data_final;
