SELECT name FROM people
JOIN stars ON people.id = stars.person_id
SELECT movie_id FROM stars WHERE people.id = (SELECT id FROM people WHERE name = 'Kevin Bacon');