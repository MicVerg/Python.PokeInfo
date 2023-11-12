SELECT "districts"."name", "expenditures"."per_pupil_expenditure"
FROM "expenditures"
WHERE "districts"."type" = 'Public School District'
JOIN "districts"
ON "expenditures"."id" = "districts"."id"
ORDER BY "expenditures"."per_pupil_expenditure" DESC
LIMIT 10;
