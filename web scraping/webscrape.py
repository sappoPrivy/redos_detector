import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
import urllib.request as ur
import json

import pandas as pd
import re

# python, java, etc
# search for "regex", import re?
# select pages / nr of results?
url = "https://api.github.com/search/code?q=regex +in:file +language:java"

# Auth Token for Github 
headers = {
  'Authorization': 'Token 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'
}

# append the found repos/users here
results = []

for i in range(1):
    # get the url content, then render html to access html parts, save as json
    req = requests.get(url, headers=headers).json()
    # print(req)

    # get the name of the repos
    results = [item["repository"]["full_name"] for item in req["items"]]
    # print(results)
    # save the file, encoding needed for windows
    with open('regex-repos-java.txt', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False)
