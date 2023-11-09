SELECT "first_name", "last_name" AS "Fattest man in MLB" FROM "players"
WHERE "weight" IS NOT NULL
ORDER BY "weight" DESC
LIMIT 1;
