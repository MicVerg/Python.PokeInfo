-- Keep a log of any SQL queries you execute as you solve the mystery.
-- first crime scene description
SELECT description
    FROM crime_scene_reports
    WHERE street = 'Humphrey Street'
    AND day = 28
    AND month = 7
    AND year = 2021;

-- check interviews of the same day
SELECT transcript
    FROM interviews
    WHERE day = 28
    AND month = 7
    AND year = 2021;

-- check license plates within 10 minutes of theft
SELECT license_plate
    FROM bakery_security_logs
    WHERE day = 28
    AND month = 7
    AND year = 2021
    AND hour = 10
    AND minute BETWEEN 15 AND 25
    AND activity = 'exit';

--