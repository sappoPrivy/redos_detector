import requests
import json
import ast

# Code can: 
# generate url for github search, "regex" inside code 
# based on file containing "user/repo" in list

filename = "web-repos-python.txt"
# filename = "web scraping/regex-repos-python.txt"

headers = {
  'Authorization': 'Token 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',
  'Accept': 'application/vnd.github.v3.text-match+json'
}

urlone = "https://github.com/"

url = "https://api.github.com/repos/"

# append the full_name
urltwo = "https://api.github.com/search/code?q=regex+in:file+repo:"

urlregex = "https://github.com/search?q=repo%3A"
# user: Flolagale
filler = "%2F" 
# repo: mailin
reg = "%20regex&type=code"

# Add all together

all_links = []

with open(filename) as file:
    for line in file:
        # dict = line
        # print(line)
        # print(type(line))
        
        dict = ast.literal_eval(line)
        print(type(dict))

        for d in dict:
            user = d.split("/")[0]
            repo = d.split("/")[1]
            link = urlregex + user + filler + repo + reg
            # print(link)
            

            linktwo = urltwo + d
            all_links.append(link)
            # req = requests.get(linktwo, headers=headers).json()
            # print(linktwo)
            # print(req)

        with open("web-regex-py-links-2.txt", 'w', encoding='utf-8') as f:
            json.dump(all_links, f, ensure_ascii=False)

