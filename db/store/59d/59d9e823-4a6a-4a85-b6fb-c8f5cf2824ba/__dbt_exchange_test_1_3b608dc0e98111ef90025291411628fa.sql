ATTACH TABLE _ UUID '8154d589-6126-4757-8e69-ac3622e53fd1'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
