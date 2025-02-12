ATTACH TABLE _ UUID 'd168a540-8d00-4565-a3de-12e927dbb5c9'
(
    `name` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS replicated_deduplication_window = 0, index_granularity = 8192
