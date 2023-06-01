import os
import requests
import urllib.parse
import json

from bs4 import BeautifulSoup
from flask import redirect, render_template, request, session
from functools import wraps

url = "https://pokeapi.co/api/v2/pokemon/"
params = {"id": "150"}

response = requests.get(url, params)

if response.status_code == 200:
    data = json.loads(response.text)
    print(data)
else:
    print(f"Error: {reponse.status_code}")