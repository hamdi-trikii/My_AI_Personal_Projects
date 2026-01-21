# AI Meeting Notes Generator (Whisper + devstral)

This application allows users to upload a recorded meeting and automatically
generates:
- A concise summary
- Key action items
- A full transcript

## Tech Stack
- Whisper (local transcription)
- devstral-small-2:24b via Ollama cloud (summarization & task extraction)
- FastAPI backend
- Streamlit frontend

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2.make a .env file and fill the blanks

 OLLAMA_API_KEY=use ur own api key from ollama

OLLAMA_HOST=https://ollama.com

BACKEND_URL=http://localhost:8000
3. Start backend:
   uvicorn backend.main:app --reload
4. Start frontend:
   streamlit run frontend/app.py