-- boring comment for boring people
SELECT score,
COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY NUMBER DESC;