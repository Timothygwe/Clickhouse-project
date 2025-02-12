
{{ config(materialized='table') }}

WITH tbl AS (
    SELECT
        name,
        DENSE_RANK() OVER (PARTITION BY craft ORDER BY name DESC) AS rank
    FROM {{ source('source_for_ranking', 'parsed_table') }}
)

SELECT name
FROM tbl
WHERE rank IN (1, 2, 3)
