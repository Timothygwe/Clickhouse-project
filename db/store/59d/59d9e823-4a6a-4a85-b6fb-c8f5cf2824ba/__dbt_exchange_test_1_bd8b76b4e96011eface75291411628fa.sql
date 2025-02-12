ATTACH TABLE _ UUID '648b0e13-33c8-45e8-8a9e-0dfd927d40ab'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
