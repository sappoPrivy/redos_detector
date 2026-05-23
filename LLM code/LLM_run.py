import requests
from datasets import load_dataset
import json
import re

LLM_OUTPUTS="LLM_output.json"
LLM_REGEXES="LLM_regexes.txt"
NUM_REG = 762

"""
Generate the regexes by prompting the LLM model.
Store the prompt and response as a JSON object in file.
"""
def generate_regexes(num_regexes, target_file):
    dataset = load_dataset("s2e-lab/RegexEval")
    subset = dataset["train"].select(range(num_regexes))

    # Load and use each prompt from the dataset
    for row in subset:
        mod_prompt = f"{row['refined_prompt']}. Respond only with the regex and nothing else and no formatting."
        prompt_request = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={"model": "llama3.1", "prompt": mod_prompt, "stream":False}
        )
        prompt_response = prompt_request.json()["response"]
        print(prompt_response)
        
        # Save the prompt and prompt output 
        with open(target_file, 'a') as t:
            prompt_record = {
                "prompt": mod_prompt,
                "regex": prompt_response
            }
            json.dump(prompt_record, t)
            t.write('\n')

"""
Extract and sanitize the regexes from the prompt outputs.
Save the regexes in a regex file.
"""
def extract_regexes(source_file, target_file):
    
    # Load and sanitize the prompt output
    with open(source_file, 'r') as s, open(target_file, 'a') as t:
        for line in s:
            prompt_record = json.loads(line)
            prompt_output = prompt_record["regex"]

            # Remove all formatting
            sanitize_regex = re.sub(r"(regex|`+|\++\*|\s+|')", "", prompt_output).strip()
            t.write(sanitize_regex + '\n')
            
def main():
    generate_regexes(NUM_REG, LLM_OUTPUTS)
    extract_regexes(LLM_OUTPUTS, LLM_REGEXES)

if __name__=="__main__":
    main()