-- lists records with same score
-- Query that lists the number of record with the same score
SELECT score, COUNT(*) AS "number"
FROM second_table
GROUP BY score
ORDER BY DESC;
