def main():
    time = input("What time is it? ")
    convert(time)

def convert(time):
    hours, minutes = time.split(':')
    hours = float(hours)
    minutes = float(minutes) / 60
    result = hours + minutes
    return result

if __name__ == "__main__":
    main()