-- lists all entries with same score
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
