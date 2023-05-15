from pyfiglet import Figlet
from cs50 import get_string
import sys
import random

figlet = Figlet()

fontList = figlet.getFonts()

#print(figlet.getFonts())
if len(sys.argv) == 1:
    input = get_string("Input: ")
    #output the text in random font from figlet.getFonts list
    randomFont = random.choice(fontList)
    figlet.setFont(font=randomFont)
    print(figlet.renderText(input))

elif len(sys.argv) == 3:
    input = get_string("Input: ")
    ##output the text with specific font from command line
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print("Usage: python figlet.py -f <font>")
        sys.exit(1)
    elif sys.argv[2] 
    else:
        fontName = sys.argv[2]
        figlet.setFont(font=fontName)
        print(figlet.renderText(input))
else:
    sys.exit(1)
