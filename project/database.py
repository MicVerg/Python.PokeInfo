import os
import requests
import urllib.parse
import json
import pprint

from bs4 import BeautifulSoup
from flask import redirect, render_template, request, session
from functools import wraps

url = "https://pokeapi.co/api/v2/pokemon/"
params = {"name": "charmander"}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = json.loads(response.text)
    pprint.pprint(data)
else:
    print(f"Error: {reponse.status_code}")