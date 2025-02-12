ATTACH TABLE _ UUID '28f33338-0f80-4cec-963d-32ff63a0c514'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192
