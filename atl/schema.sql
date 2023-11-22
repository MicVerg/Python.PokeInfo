CREATE TABLE "passengers"(
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" NUMERIC,
    PRIMARY KEY ("id")
);

CREATE TABLE "check-ins"(
    "id" INTEGER,
    "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "flight" TEXT,
    PRIMARY KEY ("id")
);

