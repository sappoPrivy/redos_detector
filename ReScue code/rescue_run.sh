#!/bin/bash

# Move to the directory of the command
cd ../ReScue-master/release

# Define input and output files
LLM_REGEXES="../../LLM code/LLM_regexes.txt"
RESULTS="../../ReScue code/rescue_results.txt"

# Ensure the output file is empty
> "$RESULTS"

# Read each regex and use input to rescue command
while IFS= read -r regex; do
    echo "### Testing $regex ###" >> "$RESULTS"
    echo "$regex" | java -jar ReScue.jar >> "$RESULTS"
    echo >> "$RESULTS"
done < "$LLM_REGEXES"
