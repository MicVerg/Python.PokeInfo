import os
import requests
import urllib.parse

from bs4 import BeautifulSoup
from flask import redirect, render_template, request, session
from functools import wraps

with open('Sandbox.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h3')
    for tag in tags:
        print(tag.text)