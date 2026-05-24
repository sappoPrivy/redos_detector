#!/bin/bash

docker pull ollama/ollama

# Start Ollama container
docker run -d --name ollama -p 11434:11434 ollama/ollama

# Pull Llama 3.1 model
docker exec -it ollama ollama pull llama3.1

echo "Done: possible to reach ollama service via http://localhost:11434"
