import requests
import json
import ast

# filename = "regex-repos-java.txt"
filename = "web scraping/regex-repos-python.txt"

headers = {
  'Authorization': 'Token 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'
}

url = "https://api.github.com/repos/"

with open(filename) as file:
    for line in file:
        # dict = line
        # print(line)
        # print(type(line))
        
        dict = ast.literal_eval(line)
        print(type(dict))

        for d in dict:
            link = url + d
            print(link)

            req = requests.get(link, headers=headers).json()
            name = d.split("/")
            name = ", ".join(name)
            openfile = name + "user.txt"
            print(openfile)

            with open(openfile, 'w', encoding='utf-8') as f:
                json.dump(req, f, ensure_ascii=False)

