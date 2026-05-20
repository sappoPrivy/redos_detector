import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
import urllib.request as ur
import json

import pandas as pd
import re

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'}

# url = "https://github.com/search?q=regex+language%3APython&type=code"
# https://github.com/search?q=web+app+language%3APython+language%3AJavaScript&type=repositories&l=JavaScript
# https://github.com/search?q=regex+language%3APython&type=code

  
# url = 'https://github.com/psf/requests'

# python, java?
url = "https://api.github.com/search/code?q=regex +in:file +language:java"

headers = {
  'Authorization': 'Token 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'
}


# append the found names here
results = []

for i in range(1):
    # get the url content, then render html to access html parts
    req = requests.get(url, headers=headers).json()
    # print(req)

    results = [item["repository"]["full_name"] for item in req["items"]]
    # print(results)
    with open('regex-repos-java.txt', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False)
