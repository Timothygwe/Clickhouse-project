ATTACH TABLE _ UUID 'a051c8a9-19b5-4626-a248-2905bcdbce14'
(
    `_inserted_at` DateTime,
    `craft` String,
    `name` String
)
ENGINE = ReplacingMergeTree
ORDER BY name
SETTINGS index_granularity = 8192
