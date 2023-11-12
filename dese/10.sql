SELECT "districts"."name", "expenditures"."per_pupil_expenditure"
FROM "expenditures"
JOIN "districts"
ON "expenditures"."id" = "districts"."id"
WHERE "districts"."type" = 'Public School District'
ORDER BY "expenditures"."per_pupil_expenditure" DESC
LIMIT 10;
