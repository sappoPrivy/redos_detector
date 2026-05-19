# Source - https://stackoverflow.com/q/74796978
# Posted by ladybug
# Retrieved 2026-05-19, License - CC BY-SA 4.0

import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
import urllib.request as ur

import pandas as pd
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'}

search_topics = "https://github.com/search?q=web&type=repositories"
# https://github.com/search?q=web+app+language%3APython+language%3AJavaScript&type=repositories&l=JavaScript
# 


dico = []

for page in range(1, 99):

    req = requests.get(search_topics + str(page) + "&q=" + "web" + "&type=Repositories", headers = headers)
    soup = BeautifulSoup(req.text, "html.parser")

    for repo in soup.select('ul.repo-list>li:has(a.v-align-middle[href])'):
        link = repo.select_one('a.v-align-middle[href]')
        about = repo.select_one('p.mb-1') 

        dico.append({
            # 'name': re.sub(r"\/(.*)\/(.*)", "\1", link.get('href')),
            'name': ' by '.join(link.text.strip().split('/', 1)[::-1]),
            'url': "https://github.com" + link.get('href'),
            'about': about.text.strip() if about else None
        })

df = pd.DataFrame(dico)

