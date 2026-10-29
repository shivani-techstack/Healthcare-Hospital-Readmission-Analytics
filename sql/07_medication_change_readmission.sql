
USE healthcare_analytics;

SELECT
    `change` AS medication_change,
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
GROUP BY `change`
ORDER BY readmission_rate_pct DESC;
