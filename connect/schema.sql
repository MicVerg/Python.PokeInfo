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

CREATE TABLE "connections"(
    "id" INTEGER,
    "user_id" INTEGER,
    "school_id" INTEGER,
    "company_id" INTEGER,
    PRIMARY KEY ("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id"),
    FOREIGN KEY ("school_id") REFERENCES "schools"("id"),
    FOREIGN KEY ("company_id") REFERENCES "companies"("id")
);
