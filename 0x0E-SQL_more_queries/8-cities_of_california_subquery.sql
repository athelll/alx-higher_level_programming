-- california

SELECT id, name
FROM cities
WHERE id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id ASC;
