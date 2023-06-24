import sys, csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except(FileNotFoundError):
        sys.exit("Could not read " + sys.argv[1] + " invalid_file.csv")