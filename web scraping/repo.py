import requests
import json
import ast

filename = "web scraping/regex-repos-java.txt"
# filename = "web scraping/regex-repos-python.txt"

headers = {
  'Authorization': 'Token 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'
}

urlone = "https://github.com/"

url = "https://api.github.com/repos/"

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
            print(link)
            all_links.append(link)
            
            # req = requests.get(link, headers=headers).json()
            # name = d.split("/")
            # name = ", ".join(name)
            # openfile = name + "user.txt"
            # print(openfile)

        with open("links-java.txt", 'w', encoding='utf-8') as f:
            json.dump(all_links, f, ensure_ascii=False)

