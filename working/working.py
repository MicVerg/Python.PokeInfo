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
        else:
            raise ValueError

if __name__ == "__main__":
    main()