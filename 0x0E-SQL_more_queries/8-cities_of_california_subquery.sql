-- california

SELECT id, name
FROM cities
WHERE id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
