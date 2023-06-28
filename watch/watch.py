import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r"<iframe.*?src="(.*?youtube\.com/embed/.*?)".*?>"


...


if __name__ == "__main__":
    main()