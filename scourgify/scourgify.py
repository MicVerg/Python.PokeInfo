import sys, csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
    except(FileNotFoundError):
        sys.exit("Could not read " + sys.argv[1] + " invalid_file.csv")