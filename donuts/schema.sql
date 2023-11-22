CREATE TABLE "ingredients"(
    "id" INTEGER,
    "name" TEXT,
    "price" INTEGER,
    "unit" TEXT,
    PRIMARY KEY ("id")
);

CREATE TABLE "donuts"(
    "id" INTEGER,
    "name" TEXT,
    "gluten-free" TEXT,
    "price" INTEGER,
    PRIMARY KEY ("id")
);

CREATE TABLE "orders"(
    "id" INTEGER,
    "ordernumber" INTEGER,
    "orderdonuts" TEXT,
    "customer" TEXT,
    "customer_id" INTEGER,
    PRIMARY KEY ("id")
    FOREIGN KEY "customer_id" REFERENCES "customers"("id")
);

CREATE TABLE "customers"(
    "id" INTEGER,
    "firstname" TEXT,
    "lastname" TEXT,
    "orderhistory" TEXT,
    PRIMARY KEY ("id")
)
