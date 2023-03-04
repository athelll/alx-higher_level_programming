-- california

SELECT cities.id, cities.name
FROM cities
WHERE id = (
	SELECT states.id
	FROM states
	WHERE states.name = 'California'
)
ORDER BY cities.id ASC;
