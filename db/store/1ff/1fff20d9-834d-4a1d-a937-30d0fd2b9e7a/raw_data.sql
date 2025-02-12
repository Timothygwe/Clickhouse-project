ATTACH TABLE _ UUID '1a12eb11-47cb-40ef-b031-d0dbb746701e'
(
    `load_time` DateTime64(6),
    `json_data` String
)
ENGINE = ReplacingMergeTree
ORDER BY json_data
SETTINGS index_granularity = 8192
