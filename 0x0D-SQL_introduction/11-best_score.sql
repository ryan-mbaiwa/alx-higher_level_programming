-- list records of the table
-- Query that list second_table records with score >= 10 ordered by descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
