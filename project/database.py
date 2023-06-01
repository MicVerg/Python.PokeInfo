import os
import requests
import urllib.parse

from bs4 import BeautifulSoup
from flask import redirect, render_template, request, session
from functools import wraps

html_text = requests.get('https://www.ictjob.be/nl/it-vacatures-zoeken?skills=411&locations=6').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'search-item.clearfix')
print(jobs)