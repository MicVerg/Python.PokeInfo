SELECT ROUND(AVG("salaries"."salary"), 2) AS "average salary", "salaries"."year"
FROM "salaries"
GROUP BY "salaries"."year"
ORDER BY "salaries"."year" DESC;
