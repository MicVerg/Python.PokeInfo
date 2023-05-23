SELECT name FROM people
JOIN stars ON movies.id = ratings.movie_id

SELECT person_id FROM stars WHERE movie_id = (SELECT id FROM movies WHERE title ='Toy Story')