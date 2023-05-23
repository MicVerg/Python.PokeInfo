SELECT DISTINCT name FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.year = 2004
ORDER BY people.birth
LIMIT 10;