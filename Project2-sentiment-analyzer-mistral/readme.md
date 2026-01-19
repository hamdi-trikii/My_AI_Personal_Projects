# Sentiment Analyzer (Mistral)

A simple AI application that uses the Mistral model via Ollama to classify text
sentiment as Positive, Negative, or Neutral.

## Features
- FastAPI backend
- Streamlit frontend
- cloud inference using Ollama-hosted Mistral

## Run Locally
1. Clone the repository
2. add a .env file and fill the blanks :
  OLLAMA_API_KEY=__ #use ur custom api key here
  OLLAMA_HOST=https://ollama.com
  BACKEND_URL=http://localhost:8000

3. Start backend:
   uvicorn backend.main:app --reload
4. Start frontend:
   streamlit run frontend/app.py
