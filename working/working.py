import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regular expression pattern to match the input formats
    pattern = r'^(\d{1,2})(?::(\d{1,2}))?\s+(AM|PM)$'

    # Match the input against the pattern
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid input format")

    # Extract the hour, minute, and period (AM/PM) from the match
    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    period = match.group(3)

    if hour < 1 or hour > 12:
        raise ValueError("Invalid hour")

    if minute < 0 or minute > 59:
        raise ValueError("Invalid minute")

    # Convert to 24-hour format
    if period == 'AM':
        if hour == 12:
            hour = 0
    elif period == 'PM':
        if hour != 12:
            hour += 12

    return f"{hour:02d}:{minute:02d}"


if __name__ == "__main__":
    main()
