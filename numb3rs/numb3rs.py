import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", "127.0.0.1", ip
    if re.search(pattern, ip):
        return True
    else:
        return False




if __name__ == "__main__":
    main()