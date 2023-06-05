import os
import requests
import json
import pprint

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pokedex", methods=["GET", "POST"])
def pokedex():
    if request.method == "GET":
        return render_template("pokedex.html")

    elif request.method == "POST":
        nameID = request.form.get("nameID")
        url = "https://pokeapi.co/api/v2/pokemon/" + nameID
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            img = data['sprites']['front_default']
            name = (data['forms'][0]['name']).capitalize()
            type = (data['types'][0]['type']['name']).capitalize()
            pokeID = data['id']
            height = data['height']
            weight = data['weight']

            # flavor text
            pokeSpecies = json.loads(requests.get("https://pokeapi.co/api/v2/pokemon-species/" + nameID).text)
            flavor_text = ""
            if pokeID >= 1 <= 151:
                for entry in pokeSpecies['flavor_text_entries']:
                    if entry['language']['name'] == 'en' and entry['version']['name'] == 'blue':
                        flavor_text = entry['flavor_text']
                        break
             elif pokeID >= 152 <= 251:
                for entry in pokeSpecies['flavor_text_entries']:
                    if entry['language']['name'] == 'en' and entry['version']['name'] == 'silver':
                        flavor_text = entry['flavor_text']
                        break
            flavor_text = flavor_text.replace('\u000c', ' ')
            return render_template("result.html", nameID=nameID, url=url, img=img, name=name, type=type, pokeID=pokeID, height=height, weight=weight, flavor_text=flavor_text)
        else:
            flash("Pokemon name or ID not found, please try again.")
            return redirect("/pokedex")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")