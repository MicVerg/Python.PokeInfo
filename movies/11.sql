SELECT title FROM movies
JOIN ratings ON movies.id = ratings.movie_id

(SELECT id FROM people WHERE name = 'Chadwick Boseman')