import sys, pip, os
from os.path import splitext
from PIL import Image, ImageOps


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
        shirt = Image.open("shirt.png")
        shirt_size = shirt.size

        photo_after = ImageOps.fit(photo_before, shirt_size)
        photo_after.paste(shirt, shirt)

        photo_after.save(sys.argv[2])

except(FileNotFoundError):
    sys.exit("Input does not exist")