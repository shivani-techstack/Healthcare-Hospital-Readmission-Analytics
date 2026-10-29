
USE healthcare_analytics;

SELECT
    time_in_hospital AS length_of_stay_days,
    COUNT(*) AS total_encounters,
    SUM(
        CASE
            WHEN readmitted = '<30' THEN 1
            ELSE 0
        END
    ) AS readmitted_within_30_days,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN readmitted = '<30' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS readmission_rate_pct
FROM diabetic_data_final
GROUP BY time_in_hospital
ORDER BY length_of_stay_days;
