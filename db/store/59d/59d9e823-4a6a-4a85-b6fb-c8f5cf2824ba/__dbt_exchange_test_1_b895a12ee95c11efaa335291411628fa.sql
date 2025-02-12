ATTACH TABLE _ UUID '25675985-c77f-41ef-9658-ed4d2118560b'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
