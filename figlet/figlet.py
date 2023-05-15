from pyfiglet import Figlet
from cs50 import get_string
import sys
import random

figlet = Figlet()

input = get_string("Input: ")
#print(figlet.getFonts())
if len(argv) == 1:
    #output the text in random font from figlet.getFonts list
    randomFont = random.choice(figlet.getFonts())
    print(f,{randomFont})
    figlet.setFont(font=randomFont)
    print(figlet.renderText(input))
elif len(argv) == 3:
    ##output the text with specific font from command line

