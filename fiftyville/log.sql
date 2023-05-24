-- Keep a log of any SQL queries you execute as you solve the mystery.
-- first crime scene description
SELECT description
    FROM crime_scene_reports
    WHERE street = 'Humphrey Street'
    AND day = 28
    AND month = 7
    AND year = 2021;

--