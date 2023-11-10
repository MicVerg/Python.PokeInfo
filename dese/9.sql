SELECT "districts"."name", MIN("expenditures"."pupils")
FROM "expenditures"
JOIN "districts"
ON "expenditures"."id" = "districts"."id"
WHERE "expenditures"."pupils" = 64;
