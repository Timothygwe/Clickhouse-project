ATTACH TABLE _ UUID '9e4fb883-58dd-4ade-a7b6-e670b6976e04'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
