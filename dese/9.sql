SELECT "districts"."name", MIN("expenditures"."pupils")
FROM "expenditures"
JOIN "districts"
ON "expenditures"."id" = "districts"."id";

SELECT "districts"."name"
FROM "districts"
WHERE "expenditures"."pupils" = (SELECT "districts"."name", MIN("expenditures"."pupils")
FROM "expenditures"
JOIN "districts"
ON "expenditures"."id" = "districts"."id");
