SELECT name FROM people
JOIN stars ON people.id = stars.person_id
WHERE id IN (SELECT person_id FROM stars)