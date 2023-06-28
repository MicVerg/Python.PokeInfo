import re
import sys

# https://regex101.com/

def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$"
    correct_format = re.search(regex, s)
    if correct_format:
        groups = correct_format.groups()
        if int(groups[1]) > 12 or int(groups[5]) > 12:
            raise ValueError
        time1 = new_format(groups[1], groups[2], groups[3])
        time2 = new_format(groups[5], groups[6], groups[7])
        return time1 + ' to ' + time2
    else:
        raise ValueError

def new_format(hour, minute, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12

    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)


    if minute == None:
        new_minute = ':00'
        new_time = f"{new_hour:02}" + new_minute
        
    else:
        new_time = f"{new_hour:02}" + ':' + minute
    return new_time


if __name__ == "__main__":
    main()