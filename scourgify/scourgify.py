import sys, csv
first_names = []
last_names = []
house = []
fieldnames = ['first', 'last', 'house']

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                first_names = row['name'].split(',')

                last_names = first_names[0]
                first_names = first_names[1]
                house = row['house']

        with open('after.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for


    except(FileNotFoundError):
        sys.exit("Could not read " + sys.argv[1] + " invalid_file.csv")