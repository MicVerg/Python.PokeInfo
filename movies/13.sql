SELECT name FROM people
JOIN stars ON people.id = stars.person_id
SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND people.birth = 1958);
