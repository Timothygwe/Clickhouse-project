ATTACH TABLE _ UUID '52f35607-56af-4a89-ad7e-473e730ada6c'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
