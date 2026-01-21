# Code Review Assistant 

This project uses the DeepSeek-Coder model via Ollama to analyze code and provide
feedback, improvement suggestions, and bug fixes.

## Features
- Code-specialized LLM devstral-small-2:24b
- FastAPI backend
- Streamlit frontend
- cloud inference with Ollama

## How to Run
1. make a .env file with those parameters :
    OLLAMA_API_KEY=uses ur own api key from ollama 

    OLLAMA_HOST=https://ollama.com

    BACKEND_URL=http://localhost:8000
    
2. Start backend:
   uvicorn backend.main:app --reload
3. Start frontend:
   streamlit run frontend/app.py
4. Paste your code and get helpful feedback