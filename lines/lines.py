import sys

# if not 1 command argument, or file ends with .py, or file doesnt exist, sys.exit
line_counter = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        with open(sys.argv[1], "r") as file:
            try:
                for line in file:
                    if not line.startswith('#') and not line.startswith(' '):
                        line_counter += 1
                print(line_counter)
            except (FileNotFoundError):
                sys.exit("File does not exist")