import requests
import json
import ast

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

all_links = []

with open(filename) as file:
    for line in file:
        # dict = line
        # print(line)
        # print(type(line))
        
        dict = ast.literal_eval(line)
        print(type(dict))

        for d in dict:
            link = urlone + d
            # print(link)
            all_links.append(link)

            linktwo = urltwo + d
            req = requests.get(linktwo, headers=headers).json()
            print(linktwo)
            print(req)

            results = [item["matches"] for item in req['text_matches']]
            
            # req = requests.get(link, headers=headers).json()
            # name = d.split("/")
            # name = ", ".join(name)
            # openfile = name + "user.txt"
            # print(openfile)

        with open("web-regex-py.txt", 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False)

