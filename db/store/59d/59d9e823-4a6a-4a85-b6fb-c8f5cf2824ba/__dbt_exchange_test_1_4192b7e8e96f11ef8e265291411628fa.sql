ATTACH TABLE _ UUID '9466844a-15ca-4b31-9b3e-a89135402fb3'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
