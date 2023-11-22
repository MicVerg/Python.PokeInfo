SELECT DISTINCT "players"."first_name", "players"."last_name"
FROM "players"
JOIN "salaries" ON "salaries"."player_id" = "players"."id"
JOIN "performances" ON "performances"."player_id" = "players"."id" AND "performances"."year" = "salaries"."year"
WHERE "players"."id" IN (
    SELECT "players"."id"
FROM "players"
JOIN "salaries" ON "salaries"."player_id" = "players"."id"
JOIN "performances" ON "performances"."player_id" = "players"."id" AND "performances"."year" = "salaries"."year"
WHERE "performances"."H" > 0 AND "performances"."year" = 2001
ORDER BY ("salaries"."salary" / "performances"."H") ASC, "players"."first_name" ASC, "players"."last_name" ASC
LIMIT 10)
AND "players"."id" IN (
    SELECT "players"."id"
FROM "players"
JOIN "salaries" ON "salaries"."player_id" = "players"."id"
JOIN "performances" ON "performances"."player_id" = "players"."id" AND "performances"."year" = "salaries"."year"
WHERE "performances"."RBI" > 0 AND "performances"."year" = 2001
ORDER BY ("salaries"."salary" / "performances"."RBI") ASC, "players"."first_name" ASC, "players"."last_name" ASC
LIMIT 10)
ORDER BY "players"."id" ASC;
