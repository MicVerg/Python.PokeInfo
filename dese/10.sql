SELECT "districts"."name", "expenditures"."per_pupil_expenditure"
FROM "expenditures"
JOIN "districts"
ON "expenditures"."id" = "districts"."id"
WHERE "expenditures"."pupils" = (SELECT MIN("pupils") FROM "expenditures");
