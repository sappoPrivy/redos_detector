#!/bin/bash

# Start Ollama container
docker run -d --name ollama -p 11434:11434 -v ollama:/root/.ollama ollama/ollama:latest

# Pull Llama 3.1 model
docker exec ollama ollama pull llama3.1

# Build ReDoS detector container
docker build -t redos_detector .

# Run detector container
docker run --rm redos_detector