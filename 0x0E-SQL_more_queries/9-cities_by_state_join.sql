-- JOINS

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ORDER BY cities.id ASC;
