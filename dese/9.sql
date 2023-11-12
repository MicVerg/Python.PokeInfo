SELECT "districts"."name"
FROM "expenditures"
JOIN "districts"
ON "expenditures"."district_id" = "districts"."id"
WHERE "expenditures"."pupils" = (SELECT MIN("pupils") FROM "expenditures");
