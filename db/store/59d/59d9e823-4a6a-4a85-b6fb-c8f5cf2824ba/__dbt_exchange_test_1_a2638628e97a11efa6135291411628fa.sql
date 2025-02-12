ATTACH TABLE _ UUID '80297642-99c4-41c7-a023-3ad8af6743bb'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
