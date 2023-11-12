SELECT "districts"."name", "expenditures"."per_pupil_expenditure", "staff_evaluation"."exemplary"
FROM "districts"
JOIN "expenditures" ON "districts"."id" = "expenditures"."district_id"
JOIN "staff_evaluation" ON "districts"."id" = "staff_evaluation"."district_id"
WHERE "expenditures"."per_pupil_expenditure" > (SELECT AVG("expenditures"."per_pupil_expenditure") FROM "expenditures")
AND

SELECT AVG("expenditures"."per_pupil_expenditure")
FROM "expenditures";
