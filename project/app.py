import os
import requests
import json

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
            if pokeID >= 152 <= 251:
                for entry in pokeSpecies['flavor_text_entries']:
                    if entry['language']['name'] == 'en' and entry['version']['name'] == 'silver':
                        flavor_text = entry['flavor_text']
                        break
            if pokeID >= 252 <= 386:
                for entry in pokeSpecies['flavor_text_entries']:
                    if entry['language']['name'] == 'en' and entry['version']['name'] == 'ruby':
                        flavor_text = entry['flavor_text']
                        break
            if pokeID >= 387 <= 493:
                for entry in pokeSpecies['flavor_text_entries']:
                    if entry['language']['name'] == 'en' and entry['version']['name'] == 'diamond':
                        flavor_text = entry['flavor_text']
                        break
            if pokeID >= 494 <= 649:
                for entry in pokeSpecies['flavor_text_entries']:
                    if entry['language']['name'] == 'en' and entry['version']['name'] == 'black':
                        flavor_text = entry['flavor_text']
                        break
            if pokeID >= 650 <= 721:
                for entry in pokeSpecies['flavor_text_entries']:
                    if entry['language']['name'] == 'en' and entry['version']['name'] == 'x':
                        flavor_text = entry['flavor_text']
                        break
            if pokeID >= 722 <= 809:
                for entry in pokeSpecies['flavor_text_entries']:
                    if entry['language']['name'] == 'en' and entry['version']['name'] == 'sun':
                        flavor_text = entry['flavor_text']
                        break
            if pokeID >= 810 <= 899:
                for entry in pokeSpecies['flavor_text_entries']:
                    if entry['language']['name'] == 'en' and entry['version']['name'] == 'sword':
                        flavor_text = entry['flavor_text']
                        break
            if pokeID >= 899 <= 905:
                for entry in pokeSpecies['flavor_text_entries']:
                    if entry['language']['name'] == 'en' and entry['version']['name'] == 'legends-arceus':
                        flavor_text = entry['flavor_text']
                        break
            # fix u000c
            flavor_text = flavor_text.replace('\u000c', ' ')

            # evolves into
            current_pokemon = None
            for evolution in evolutionChain:
                if evolution['species']['name'] == name:
                    current_pokemon = evolution
                    break

            if current_pokemon and 'evolves_to' in current_pokemon:
                next_evolution = current_pokemon['evolves_to'][0]['species']
                next_evolution_name = next_evolution['name'].capitalize()
                next_evolution_url = next_evolution['url']
                next_evolution_id = int(re.search(r'/(\d+)/$', next_evolution_url).group(1))
            else:
                next_evolution_name = None
                next_evolution_url = None
                next_evolution_id = None

            else:
                evolutionImg = "/static/icons8-no-entry-80.png"
            return render_template("result.html", nameID=nameID, url=url, img=img, name=name, type=type, pokeID=pokeID, height=height, weight=weight, flavor_text=flavor_text, pokeEvolution=pokeEvolution, evolutionImg=evolutionImg)


        else:
            flash("Pokemon name or ID not found, please try again.")
            return redirect("/pokedex")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")