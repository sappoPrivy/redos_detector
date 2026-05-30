#!/bin/bash

# Move to the directory of the command
cd ../ReScue-master/release

# Define input and output files
LLM_REGEXES="../../LLM code/LLM_regexes.txt"
LLM_RESULTS="../../ReScue code/rescue_llm_results.txt"
GIT_RESULTS="../../ReScue code/rescue_git_results.txt"
GIT_REGEXES="../../web scraping/repo-python.txt"

# Ensure the output file is empty
> "$GIT_RESULTS"

# Read each regex and use input to rescue command
while IFS= read -r regex; do
    echo "### Testing $regex ###" >> "$GIT_RESULTS"
    echo "$regex" | java -jar ReScue.jar >> "$GIT_RESULTS"
    echo >> "$GIT_RESULTS"
done < "$GIT_REGEXES"
