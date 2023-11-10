SELECT "city", COUNT(id) AS "Total_amount_of_schools"
FROM "schools"
WHERE "type" = 'Public School'
GROUP BY "city"

