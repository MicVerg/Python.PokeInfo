SELECT title FROM movies
JOIN stars on movies.id = stars.movie_id
WHERE stars.person_id = (SELECT id FROM people WHERE name = 'Johnny Depp')
AND title IN
(SELECT title FROM movies
JOIN stars on movies.id = stars.movie_id
WHERE stars.person_id IN (SELECT id FROM people WHERE name = 'Helena Bonham Carter'));