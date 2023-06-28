import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r"<iframe.*?src="(.*?youtube\.com/embed/.*?)".*?>"
    URL = re.findall(regex, s)

    if re.findall(regex, s):
        return URL




if __name__ == "__main__":
    main()