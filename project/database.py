import os
import requests
import urllib.parse

from bs4 import BeautifulSoup
from flask import redirect, render_template, request, session
from functools import wraps

url = "https://pokeapi.co/api/v2/pokemon/"
params = {"squirtle"}

response = requests.get(url, params)