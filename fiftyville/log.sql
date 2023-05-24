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

-- check combo of person IDs and license plates, these are the names of people who were at bakery + withdrew SUSPECT LIST
SELECT DISTINCT name FROM people
    JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
    WHERE people.id IN
        (SELECT person_id FROM bank_accounts
        JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
        WHERE bank_accounts.account_number IN
            (SELECT account_number FROM atm_transactions
            WHERE DAY = 28
            AND MONTH = 7
            AND year = 2021
            AND transaction_type = 'withdraw'
            AND atm_location = 'Leggett Street'));

-- check phone calls, thief is CALLER
SELECT caller
    FROM phone_calls
    WHERE duration < 60
    AND DAY = 28
    AND MONTH = 7
    AND year = 2021;

-- check caller phone list against suspect list
SELECT DISTINCT name
    FROM people
    JOIN phone_calls ON phone_calls.caller = people.phone_number
    WHERE caller IN
        (SELECT caller
        FROM phone_calls
        WHERE duration < 60
        AND DAY = 28
        AND MONTH = 7
        AND year = 2021
        AND name IN
            (SELECT DISTINCT name FROM people
            JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
            WHERE people.id IN
                (SELECT person_id FROM bank_accounts
                JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
                WHERE bank_accounts.account_number IN
                    (SELECT account_number
                    FROM atm_transactions
                    WHERE DAY = 28
                    AND MONTH = 7
                    AND year = 2021
                    AND transaction_type = 'withdraw'
                    AND atm_location = 'Leggett Street')))); -- SUSPECT LIST


-- ID of fiftyville
SELECT id
    FROM airports
    WHERE city = 'Fiftyville';

-- check the earliest flight on 29/7/2021 (ID)
SELECT DISTINCT destination_airport_id, id
    FROM flights
    WHERE day = 29
    AND month = 7
    AND year = 2021
    AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
    ORDER BY hour, minute ASC
    LIMIT 1;

-- check what airport that ID is
SELECT city
    FROM airports
    WHERE id = (SELECT DISTINCT destination_airport_id
    FROM flights
        WHERE day = 29
        AND month = 7
        AND year = 2021
        AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
        ORDER BY hour, minute ASC
        LIMIT 1);

-- check passport numbers that are on the suspects flight
SELECT passport_number
    FROM passengers
    WHERE flight_id = ((SELECT DISTINCT id
    FROM flights
    WHERE day = 29
    AND month = 7
    AND year = 2021
    AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
    ORDER BY hour, minute ASC
    LIMIT 1));

-- check passport numbers to names
SELECT DISTINCT name
    FROM people
    JOIN passengers ON passengers.passport_number = people.passport_number
    WHERE people.passport_number IN
    (SELECT passport_number
        FROM passengers
        WHERE flight_id = ((SELECT DISTINCT id
            FROM flights
            WHERE day = 29
            AND month = 7
            AND year = 2021
            AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
            ORDER BY hour, minute ASC
            LIMIT 1)));

--names of suspects on flight
SELECT DISTINCT name
    FROM people
    JOIN phone_calls ON phone_calls.caller = people.phone_number
    WHERE caller IN
        (SELECT caller
        FROM phone_calls
        WHERE duration < 60
        AND DAY = 28
        AND MONTH = 7
        AND year = 2021
        AND name IN
            (SELECT DISTINCT name
            FROM people
            JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
            WHERE people.id IN
                (SELECT person_id
                FROM bank_accounts
                JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
                WHERE bank_accounts.account_number IN
                    (SELECT account_number
                    FROM atm_transactions
                    WHERE DAY = 28
                    AND MONTH = 7
                    AND year = 2021
                    AND transaction_type = 'withdraw'
                    AND atm_location = 'Leggett Street')))
        AND caller in (SELECT DISTINCT people.phone_number
        FROM people
        JOIN passengers ON passengers.passport_number = people.passport_number
        WHERE people.passport_number IN
            (SELECT passport_number
            FROM passengers
            WHERE flight_id = ((SELECT DISTINCT id
                FROM flights
                WHERE day = 29
                AND month = 7
                AND year = 2021
                AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
                ORDER BY hour, minute ASC
                LIMIT 1)))));

-- check who THIEF called
SELECT DISTINCT receiver
    FROM phone_calls
    WHERE caller = (SELECT phone_number FROM people WHERE name = 'Bruce')
    AND duration < 60
    AND DAY = 28
    AND MONTH = 7
    AND year = 2021;

-- check that person's name ACCOMPLICE
SELECT DISTINCT name
    FROM people
    JOIN phone_calls ON phone_calls.receiver = people.phone_number
    WHERE receiver =
        (SELECT DISTINCT receiver
        FROM phone_calls
        WHERE caller = (SELECT phone_number FROM people WHERE name IN ('Kenny', 'Taylor', 'Bruce'))
        AND duration < 60
        AND DAY = 28
        AND MONTH = 7
        AND year = 2021);

-- check thief
SELECT caller
    FROM phone_calls
    JOIN people ON phone_calls.receiver = people.phone_number
    WHERE phone_calls.receiver = '(375) 555-8161'
    AND duration < 60
    AND DAY = 28
    AND MONTH = 7
    AND year = 2021;

-- check thief name
SELECT DISTINCT name
    FROM people
    JOIN phone_calls ON phone_calls.caller = people.phone_number
    WHERE phone_calls.caller =
        (SELECT caller
        FROM phone_calls
        JOIN people ON phone_calls.receiver = people.phone_number
        WHERE phone_calls.receiver = '(375) 555-8161'
        AND duration < 60
        AND DAY = 28
        AND MONTH = 7
        AND year = 2021);

-- accomplice name
SELECT DISTINCT name
    FROM people
    JOIN phone_calls ON phone_calls.receiver = people.phone_number
    WHERE phone_calls.receiver = '(375) 555-8161';