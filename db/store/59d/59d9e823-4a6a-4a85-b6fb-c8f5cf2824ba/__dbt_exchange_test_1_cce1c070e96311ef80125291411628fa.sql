ATTACH TABLE _ UUID '1f4fe253-f909-414f-9335-ddd70fcd29e9'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
