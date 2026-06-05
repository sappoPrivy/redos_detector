# Evaluation of ReDoS Detection Tools on LLM‑Generated Regexes vs. GitHub Regexes

This project evaluates three ReDoS detection tools: **ReDoSHunter**, **ReScue**, and **Regexploit** on two regex populations:

1. **LLM‑generated regexes using Ollama**
2. **Regexes extracted from real GitHub repositories**

The goal is to compare detection coverage, identify which ReDoS pattern types occur in each dataset, and understand how the tools complement each other.  
ReDoSHunter plays a central role due to its combined **static + dynamic** analysis, which detects five ReDoS pattern types (POA, SLQ, EOA, EOD, NQ) and fuzzes suspicious regexes to confirm vulnerabilities.

---

## Overview of the Project

- **LLM Automation Pipeline**  
  Generates regexes using the Ollama engine (llama3.1), sanitizes outputs, and stores them for analysis.

- **ReDoSHunter**  
  Java‑based tool combining static pattern detection with dynamic fuzzing. Used to classify regexes into ReDoS pattern types and confirm vulnerabilities.

- **ReScue**  
  Java tool using genetic search + dynamic testing to detect catastrophic backtracking.

- **Regexploit**  
  Static‑only heuristic detector that identifies exponential‑time regex structures.

- **GitHub Regex Collection**  
  Regexes scraped from real web‑application repositories using the GitHub REST API.

---

## Prerequisites & Dependencies

### General Requirements
- Python 3  
- Java Runtime Environment (JRE)  
- Docker (for running Ollama)  
- GitHub API token (for scraping repos)

---

### LLM Automation Pipeline
- Python packages (venv recommended)
- Ollama engine + llama3.1 model  
- Scripts:
  - `LLM_run.py`
  - `ollama_run.sh`

---

### ReDoSHunter
- Java 8+  
- Gradle  
- Modified `Test.java` for input/output paths  
- Input files:
  - `regex-762.txt`, `regex-100.txt`
  - `git-regex.txt`
- Output directory: `RESULTS/`

**Repository:**  
🔗 https://github.com/Silv-ia/ReDoSHunter-DD2525-project

---

### ReScue
- Java Runtime Environment  
- `ReScue.jar` (included in `/ReScue-master`)  
- Script:
  - `rescue_run.sh`

---

### Regexploit
- Python  
- Installed `regexploit` tool  
- Script:
  - `regexploit_run.py`

---

### GitHub Regex Scraper
- Python  
- GitHub API token  
- Scripts:
  - `webscrape.py`
  - `repo.py`

---

## Results

### Table 3 — LLM Regexes

| ReDoS Pattern Type | ReDoSHunter | Regexploit | ReScue |
|--------------------|-------------|------------|--------|
| POA                | 15          | 1          | 0      |
| SLQ                | 19          | 0          | 0      |
| EOA                | 1           | 2          | 0      |
| EOD                | 0           | 0          | 0      |
| NQ                 | 0           | 1          | 1      |
| **Total**          | **35**      | **4**      | **1**  |

*Only one overlapping vulnerability detected: regex 437 (ReDoSHunter + Regexploit).*

---

### Table 4 — GitHub Regexes

| ReDoS Pattern Type | ReDoSHunter | Regexploit | ReScue |
|--------------------|-------------|------------|--------|
| POA                | 5           | 0          | 0      |
| SLQ                | 7           | 1          | 1      |
| EOA                | 0           | 0          | 0      |
| EOD                | 0           | 0          | 0      |
| NQ                 | 0           | 0          | 0      |
| **Total**          | **12**      | **1**      | **1**  |

*Only one overlapping vulnerability detected: regex 18.*

---

## Repository Links

- **ReDoSHunter Project**  
  https://github.com/Silv-ia/ReDoSHunter-DD2525-project

- **ReDoS Detectors Repository**  
  https://github.com/sappoPrivy/redos_detector

---

## Authors
Tenzin Sangpo Choedon  
Silvia Lü  
Group 23 — DD2525
