ATTACH TABLE _ UUID '79dbd62e-b408-4486-852f-17d0979dc038'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
