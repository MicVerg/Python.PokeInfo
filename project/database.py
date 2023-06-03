import os
import requests
import urllib.parse
import json
import pprint

from bs4 import BeautifulSoup
from flask import redirect, render_template, request, session
from functools import wraps

pokeString = input("Enter a pokemon name or id: ")
url = "https://pokeapi.co/api/v2/pokemon/" + pokeString
# params = {"id": "10"}


response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    pokemonName = data['types'][0]['type']['name']
    pprint.pprint(data)
    print(response.url)
    print("That pokemon is " + pokemonName)
else:
    print(f"Error: {reponse.status_code}")