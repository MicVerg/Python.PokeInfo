SELECT name FROM people

SELECT movie_id FROM stars WHERE person.id = (SELECT id FROM people WHERE name = 'Kevin Bacon')
JOIN stars ON people.id = stars.person_id;