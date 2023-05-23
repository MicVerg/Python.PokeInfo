SELECT title FROM movies
JOIN stars on movies.id = stars.movie_id
WHERE stars.person_id IN (SELECT id FROM people WHERE name = 'Johnny Depp' INTERSECT SELECT id FROM people WHERE name = 'Helena Bonham Carter');