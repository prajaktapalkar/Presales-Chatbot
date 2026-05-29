# AI Presales Chatbot (RAG-Based)

A Retrieval-Augmented Generation (RAG) chatbot built using:

* Flask
* LangChain
* FAISS Vector Database
* HuggingFace Embeddings
* Ollama
* Phi-3 Mini Local LLM

## Features

* Upload company/networking documents
* Semantic document search
* Local vector database using FAISS
* Fully local AI inference using Ollama
* REST API chatbot endpoint
* No paid APIs required

---

## Tech Stack

* Python
* Flask
* LangChain
* FAISS
* HuggingFace Sentence Transformers
* Ollama
* Phi-3 Mini

---

## Project Structure

```text
presales-chatbot/
│
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
├── docs/
├── vectorstore/
└── .env
```

---

## Installation

### Clone repository

```bash
git clone <your-repo-url>
cd presales-chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download:
https://ollama.com/download/windows

Run model:

```bash
ollama run phi3:mini
```

---

## Create Vector Database

Place PDFs inside:

```text
docs/
```

Then run:

```bash
python ingest.py
```

---

## Run Chatbot

```bash
python app.py
```

Server starts at:

```text
http://127.0.0.1:5000
```

---

## Test API

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/chat" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"message":"What services do you provide?"}'
```

---

## Example Use Cases

* Presales support assistant
* Company knowledge chatbot
* Networking solutions assistant
* Internal documentation search
* Local/offline RAG system

---

## Future Improvements

* Web frontend UI
* Streamlit interface
* Chat history
* Authentication
* Docker deployment
* Multi-document upload
