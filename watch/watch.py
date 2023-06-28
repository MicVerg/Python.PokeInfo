import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r'<iframe.*?src=".*?youtube\.com/embed/(.*?)".*?>'
    URL = re.search(regex, s)

    if URL:
        return URL.group(1)
    else:
        return None



if __name__ == "__main__":
    main()