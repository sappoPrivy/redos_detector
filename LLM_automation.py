import requests
from datasets import load_dataset
import csv
import os
import json
import re


def generate_regexes(num_regexes):
    dataset = load_dataset("s2e-lab/RegexEval")

    for row in dataset["train"]:
        r = requests.post(
        "http://127.0.0.1:11434/api/generate",
        json={"model": "llama3.1", "prompt": f"{row['refined_prompt']}. Respond only with the regex.", "stream":False}
        )
        print(r.json()["response"])

        with open('LLM_regexes3.json', 'a') as f:
            prompt = f"{row['refined_prompt']}. Respond only with the regex and nothing else and no formatting at all."
            response_text = r.json()["response"]
            data = {
            "prompt": prompt,
            "regex": response_text
            }
            json.dump(data, f)
            f.write('\n')

def extract_regexes():
    with open('LLM_regexes3.json', 'r') as jsonFile, open('LLM_regexes5.txt', 'a') as txtFile:
        for l in jsonFile:
            obj = json.loads(l)
            output = obj["regex"]
            # txtFile.write(obj["regex"]+"\n")
            # Remove unnecessary formatting using regular expression
            # pattern = re.sub(r'^```\n(.*)\n```$', r'\1', obj["regex"])
            # txtFile.write(pattern + '\n')
            
            # Remove all types of formatting
            output = output.replace('\n', '')
            output = output.replace('regex', '')
            output = output.replace('\t', '')
            output = output.replace('```', '')
            output = output.replace('+++*', '')
            output = output.replace("'", '')
            output = output.strip()
            
            txtFile.write(output + '\n')
            



def main():
    #generate_regexes()
    extract_regexes()

if __name__=="__main__":
    main()