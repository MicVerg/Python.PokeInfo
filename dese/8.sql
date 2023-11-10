SELECT "districts"."name", "expenditures"."pupils"
FROM "expenditures"
JOIN "districts"
ON "expenditures"."id" = "districts"."id";
