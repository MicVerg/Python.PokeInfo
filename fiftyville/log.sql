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

-- check combo of ATM withdrawal before 10:15 on Leggett street and license plates bakery
SELECT account_number
    FROM atm_transactions
    WHERE DAY = 28
    AND MONTH = 7
    AND year = 2021
    AND transaction_type = 'withdraw'
    AND atm_location = 'Leggett Street';

-- check person_id based on ATM withdrawals of theft day
SELECT person_id FROM bank_accounts
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
    WHERE bank_accounts.account_number IN
        (SELECT account_number FROM atm_transactions
        WHERE DAY = 28
        AND MONTH = 7
        AND year = 2021
        AND transaction_type = 'withdraw'
        AND atm_location = 'Leggett Street');
