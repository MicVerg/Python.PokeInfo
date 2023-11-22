CREATE TABLE "users"(
    "id" INTEGER,
    "firstname" TEXT,
    "lastname" TEXT,
    "username" TEXT,
    "password" TEXT,
    PRIMARY KEY ("id")
);

CREATE TABLE "schools"(
    "id" INTEGER,
    "schoolname" TEXT,
    "schooltype" TEXT,
    "location" TEXT,
    "foundingyear" NUMERIC,
    PRIMARY KEY ("id")
);

CREATE TABLE "companies"(
    "id" INTEGER,
    "companyname" TEXT,
    "industry" TEXT,
    "location" TEXT,
    PRIMARY KEY ("id")
);
