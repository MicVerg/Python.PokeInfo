-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description
    FROM crime_scene_reports
    WHERE street IN 'Humphrey Street'
    AND day IN 28
    AND month IN 7
    AND year IN 2021;