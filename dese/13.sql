SELECT "graduation_rates"."dropped", "schools"."name"
FROM "graduation_rates"
JOIN "schools" ON "graduation_rates"."school_id" = "schools"."id"
ORDER BY "graduation_rates"."dropped" DESC
LIMIT 10;
