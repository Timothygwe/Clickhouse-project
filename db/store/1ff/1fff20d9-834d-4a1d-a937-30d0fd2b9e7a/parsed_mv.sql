ATTACH MATERIALIZED VIEW _ UUID 'ba9c4475-f5c9-4304-9816-ff9d5d916d0f' TO default.parsed_table
(
    `_inserted_at` DateTime,
    `craft` String,
    `name` String
)
AS SELECT
    now() AS _inserted_at,
    JSONExtractString(json_data, 'craft') AS craft,
    JSONExtractString(json_data, 'name') AS name
FROM default.raw_data
