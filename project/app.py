import requests
import json
import re

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pokedex", methods=["GET", "POST"])
def pokedex():
    nameID = None
    # GET
    if request.method == "GET":
        nameID = (request.args.get("nameID"))
        if nameID:
            url = "https://pokeapi.co/api/v2/pokemon/" + nameID
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.text)
                img = data['sprites']['front_default']
                name = (data['forms'][0]['name'])
                type = (data['types'][0]['type']['name'])
                pokeID = data['id']
                height = data['height']
                weight = data['weight']
                pokeIDPrevious = pokeID - 1
                pokeIDNext = pokeID + 1

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

                # fix flavor text
                flavor_text = flavor_text.replace('\u000c', ' ')
                # thanks @Chiaki(MalevolentAntichrist#3741) and @Mao(mao_sz) from discord for the solution below, I had been looking for ages .. !!!
                flavor_text = flavor_text.replace("&shy", '').replace("\xad\n","")

                # evolves into
                pokeEvolution, evolutionName, evolutionID = "", "", ""
                evolutionImg = "/static/icons8-no-entry-80.png"
                url = pokeSpecies['evolution_chain']['url']
                evolutionChain = json.loads(requests.get(url).text)['chain']
                try:
                    if 'evolves_to' in evolutionChain and name == evolutionChain['species']['name']:
                        try:
                            first_evolution = evolutionChain['evolves_to'][0]
                            pokeEvolution = first_evolution['species']['url']
                            evolutionResponse = requests.get(pokeEvolution)
                            evolutionData = json.loads(evolutionResponse.text)
                            evolutionID = evolutionData['id']
                            evolutionImg = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon/" + str(evolutionID))).text))['sprites']['front_default']
                            evolutionName = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon/" + str(evolutionID))).text))['forms'][0]['name']
                        except IndexError:
                            second_evolution = None

                    elif 'evolves_to' in evolutionChain and name == evolutionChain['evolves_to'][0]['species']['name']:
                        try:
                            second_evolution = evolutionChain['evolves_to'][0]['evolves_to'][0]
                            pokeEvolution = second_evolution['species']['url']
                            evolutionResponse = requests.get(pokeEvolution)
                            evolutionData = json.loads(evolutionResponse.text)
                            evolutionID = evolutionData['id']
                            evolutionImg = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon/" + str(evolutionID))).text))['sprites']['front_default']
                            evolutionName = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon/" + str(evolutionID))).text))['forms'][0]['name']
                        except IndexError:
                            second_evolution = None
                except IndexError:
                    first_evolution = None
                    second_evolution = None
                # evolves from
                evolutionFromName = ""
                evolutionFromImg = "/static/icons8-no-entry-80.png"
                evolutionFrom = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon-species/" + str(pokeID))).text))
                if 'evolves_from_species' in evolutionFrom and evolutionFrom['evolves_from_species'] is not None:
                    evolutionFromName = evolutionFrom['evolves_from_species']['name']
                    evolutionFromImg = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon/" + str(evolutionFromName))).text))['sprites']['front_default']

                return render_template("result.html", nameID=nameID, url=url, img=img, name=name, type=type, pokeID=pokeID, height=height, weight=weight, flavor_text=flavor_text, pokeEvolution=pokeEvolution, evolutionImg=evolutionImg, evolutionName=evolutionName, evolutionID=evolutionID, evolutionFromImg=evolutionFromImg, evolutionFromName=evolutionFromName, pokeIDPrevious=pokeIDPrevious, pokeIDNext=pokeIDNext)
            else:
                flash("Pokemon name or ID not found, please try again.")
        return render_template("pokedex.html")

    # POST
    elif request.method == "POST":
        nameID = (request.form.get("nameID")).lower()
        if not nameID:
            flash("Please enter a Pokemon name or ID.")
            return redirect("/pokedex")

        url = "https://pokeapi.co/api/v2/pokemon/" + nameID
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            img = data['sprites']['front_default']
            name = (data['forms'][0]['name'])
            type = (data['types'][0]['type']['name'])
            pokeID = data['id']
            height = data['height']
            weight = data['weight']
            pokeIDPrevious = pokeID - 1
            pokeIDNext = pokeID + 1

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

            # fix flavor text
            flavor_text = flavor_text.replace('\u000c', ' ')
            # thanks @Chiaki(MalevolentAntichrist#3741) and @Mao(mao_sz) from discord for the solution below, I had been looking for ages .. !!!
            flavor_text = flavor_text.replace("&shy", '').replace("\xad\n","")

            # evolves into
            pokeEvolution, evolutionName, evolutionID = "", "", ""
            evolutionImg = "/static/icons8-no-entry-80.png"
            url = pokeSpecies['evolution_chain']['url']
            evolutionChain = json.loads(requests.get(url).text)['chain']
            if 'evolves_to' in evolutionChain and name == evolutionChain['species']['name']:
                try:
                    first_evolution = evolutionChain['evolves_to'][0]
                    pokeEvolution = first_evolution['species']['url']
                    evolutionResponse = requests.get(pokeEvolution)
                    evolutionData = json.loads(evolutionResponse.text)
                    evolutionID = evolutionData['id']
                    evolutionImg = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon/" + str(evolutionID))).text))['sprites']['front_default']
                    evolutionName = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon/" + str(evolutionID))).text))['forms'][0]['name']
                except IndexError:
                    second_evolution = None

            elif 'evolves_to' in evolutionChain and name == evolutionChain['evolves_to'][0]['species']['name']:
                try:
                    second_evolution = evolutionChain['evolves_to'][0]['evolves_to'][0]
                    pokeEvolution = second_evolution['species']['url']
                    evolutionResponse = requests.get(pokeEvolution)
                    evolutionData = json.loads(evolutionResponse.text)
                    evolutionID = evolutionData['id']
                    evolutionImg = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon/" + str(evolutionID))).text))['sprites']['front_default']
                    evolutionName = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon/" + str(evolutionID))).text))['forms'][0]['name']
                except IndexError:
                    second_evolution = None

            # evolves from
            pokeEvolutionFrom, evolutionFromName, evolutionFromID = "", "", ""
            evolutionFromImg = "/static/icons8-no-entry-80.png"
            evolutionFrom = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon-species/" + str(pokeID))).text))
            if 'evolves_from_species' in evolutionFrom and evolutionFrom['evolves_from_species'] is not None:
                evolutionFromName = evolutionFrom['evolves_from_species']['name']
                evolutionFromImg = (json.loads((requests.get("https://pokeapi.co/api/v2/pokemon/" + str(evolutionFromName))).text))['sprites']['front_default']

            return render_template("result.html", nameID=nameID, url=url, img=img, name=name, type=type, pokeID=pokeID, height=height, weight=weight, flavor_text=flavor_text, pokeEvolution=pokeEvolution, evolutionImg=evolutionImg, evolutionName=evolutionName, evolutionID=evolutionID, evolutionFromImg=evolutionFromImg, evolutionFromName=evolutionFromName, pokeIDPrevious=pokeIDPrevious, pokeIDNext=pokeIDNext)
        else:
            flash("Pokemon name or ID not found, please try again.")
            return redirect("/pokedex")
