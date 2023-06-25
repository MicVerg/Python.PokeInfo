import sys, pip, os
from os.path import splitext

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif splitext(sys.argv[1])[1] != '.jpg' or splitext(sys.argv[1])[1] != '.jpeg' or splitext(sys.argv[1])[1] != '.png':
    sys.exit("Invalid input")
elif splitext(sys.argv[2])[1] != '.jpg' or splitext(sys.argv[2])[1] != '.jpeg' or splitext(sys.argv[2])[1] != '.png':
    sys.exit("Invalid output")
elif splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
    sys.exit("Input and output have different extensions")
