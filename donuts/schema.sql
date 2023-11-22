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
    PRIMARY KEY ("id")
)
