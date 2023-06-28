import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r'<iframe.*?src="(.*?youtube\.com/embed/.*?)".*?>'
    URL = re.search(regex, s)

    if re.search(regex, s):
        return URL
    else:
        None



if __name__ == "__main__":
    main()