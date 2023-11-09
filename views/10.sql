SELECT "artist" AS "Highest entropy artist" FROM "views"
WHERE "brightness" < 1 AND "brightness" > 0
ORDER BY "entropy" DESC
LIMIT 1;
