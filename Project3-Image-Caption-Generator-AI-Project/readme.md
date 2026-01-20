# Image Caption Generator (qween3-lv)

This project uses the qween3-lv vision-language model via Ollama to generate descriptive
captions for uploaded images.

## Features
- Vision-language model
- FastAPI backend
- Streamlit UI

## How to Run
1. make a .env file and fill the blanks 
    OLLAMA_API_KEY=uses ur own api key from ollama 

    OLLAMA_HOST=https://ollama.com

    BACKEND_URL=http://localhost:8000
2. Start backend:
   uvicorn backend.main:app --reload
3. Start frontend:
   streamlit run frontend/app.py
4. Upload an image and generate a caption
