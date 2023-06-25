import sys, pip, os


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif splitext(argv[1])[1] != '.jpg' or splitext(argv[1])[1] != '.jpeg' or splitext(argv[1])[1] != '.png':
    sys.exit("Invalid output")
else: