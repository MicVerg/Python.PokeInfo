from pyfiglet import Figlet
from cs50 import get_string
from sys import argv

figlet = Figlet()

input = get_string("Input: ")
#print(figlet.getFonts())
if len(argv) == 0:
    #output the text in random font from figlet.getFonts list
elif len(argv) == 2:
    ##output the text with specific font from command line
    
