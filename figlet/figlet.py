from pyfiglet import Figlet
from cs50 import get_string
from sys import argv

figlet = Figlet()

input = get_string("Input: ")
print(figlet.getFonts())

