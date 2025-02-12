ATTACH TABLE _ UUID 'fcd8edd2-27f1-45c2-b493-240989dc9d9c'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
