SELECT name FROM people
JOIN stars ON people.id = stars.person_id
WHERE id IN 
SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND (SELECT id FROM people WHERE birth = 1958));