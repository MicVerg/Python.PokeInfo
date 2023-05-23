SELECT name FROM people
JOIN stars ON people.id = stars.person_id
SELECT movie_id FROM stars = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958);