import sys, pip, os
from os.path import splitext
from PIL import Image


try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if splitext(sys.argv[1])[1] != '.jpg' and splitext(sys.argv[1])[1] != '.jpeg' and splitext(sys.argv[1])[1] != '.png':
        sys.exit("Invalid input")
    if splitext(sys.argv[2])[1] != '.jpg' and splitext(sys.argv[2])[1] != '.jpeg' and splitext(sys.argv[2])[1] != '.png':
        sys.exit("Invalid output")
    if splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")
    else:
        photo_before = Image.open(sys.argv[1])
        photo_before_size = photo_before.size
        shirt = Image.open("shirt.png")
        photo_before.paste(shirt, shirt)

except(FileNotFoundError):
    sys.exit("Input does not exist")