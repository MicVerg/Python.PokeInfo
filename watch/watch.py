import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r'<iframe.*?src=".*?youtube\.com/embed/(.*?)".*?>'
    URL = re.search(regex, s)

    if URL:
        video_id = URL.group(1)
        youtube_link = f"https://youtu.be/{video_id}"
        return youtube_link
    else:
        return None


if __name__ == "__main__":
    main()
