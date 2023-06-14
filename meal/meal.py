def main():
    time = input("What time is it? ")
    timeFloat = convert(time)

    if timeFloat >= 7 and timeFloat <= 8:
        print("breakfast time")
    if timeFloat >= 12 and timeFloat <= 13:
        print("lunch time")
    if timeFloat >= 18 and timeFloat <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes) / 60
    result = hours + minutes
    return result

if __name__ == "__main__":
    main()