CREATE TABLE "passengers"(
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" NUMERIC,
    PRIMARY KEY ("id")
);

CREATE TABLE "check-ins"(
    "id" INTEGER,
    "passenger_id" INTEGER,
    "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "flight" TEXT,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("passenger_id") REFERENCES "passengers"("id")
);

CREATE TABLE "airlines"(
    "id" INTEGER,
    "name" TEXT,
    "concourses" TEXT,
    PRIMARY KEY ("id")
);
