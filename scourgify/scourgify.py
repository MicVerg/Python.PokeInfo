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
                name_parts = row['name'].split(',')

                last_names.append(name_parts[0].strip())
                first_names.append(name_parts[1].strip())
                house.append(row['house'])

        with open('after.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for i in range(len(first_names)):
                writer.writerow({
                    'first': first_names[i],
                    'last': last_names[i],
                    'house': house[i]
                })

    except(FileNotFoundError):
        sys.exit("Could not read " + sys.argv[1] + " invalid_file.csv")