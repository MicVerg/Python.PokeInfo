SELECT "city", COUNT(id) AS "Total_amount_of_schools"
FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city" < 3
ORDER BY "Total_amount_of_schools" DESC, "city" ASC;
