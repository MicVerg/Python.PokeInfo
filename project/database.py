import os
import requests
import urllib.parse

from bs4 import BeautifulSoup
from flask import redirect, render_template, request, session
from functools import wraps

html_text = requests.get('https://www.vdab.be/vindeenjob/vacatures?trefwoord=python&locatie=West-Vlaanderen%20(Provincie)&locatieCode=BE25&sort=standaard&sinds=6&arbeidscircuit=8').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'panel-body')
print(jobs)