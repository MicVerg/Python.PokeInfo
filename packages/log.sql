
-- *** The Lost Letter ***
SELECT * FROM "packages"
WHERE "from_address_id" = '900 Somerville Avenue';

SELECT * FROM "packages"
   ...> LIMIT 10;

SELECT * FROM "addresses"
LIMIT 10;

SELECT * FROM "packages"
WHERE "from_address_id" = (SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue') AND "to_address_id" = (SELECT "id" FROM "addresses" WHERE "address" = '%Finnigan Street%');

SELECT * FROM "packages"
WHERE "contents" LIKE '%Congratulatory%';

SELECT * FROM "scans"
WHERE "package_id" = 384;

SELECT * FROM "addresses"
WHERE "address_id" = 854;

-- *** The Devious Delivery ***

-- *** The Forgotten Gift ***

