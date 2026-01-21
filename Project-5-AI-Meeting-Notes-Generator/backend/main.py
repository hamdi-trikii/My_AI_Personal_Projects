from fastapi import FastAPI, UploadFile, File
from contextlib import asynccontextmanager
import whisper

import tempfile
import os
from ollama import Client
from dotenv import load_dotenv



#load api key from .env file
load_dotenv()
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "https://ollama.com")

# Initialize Ollama client
client = Client(
    host=OLLAMA_HOST,
    headers={'Authorization': f'Bearer {OLLAMA_API_KEY}'}
)

app = FastAPI()

# Load Whisper model (use 'small' for better accuracy if needed)
model = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global model
    model = whisper.load_model("base")
    yield
    # Shutdown
    pass

app = FastAPI(lifespan=lifespan)

#ministral-3:14b
def call_ollama(prompt: str) -> str:

    messages = [
        {"role": "user", "content": prompt}
    ]
    response = client.chat(
        model="devstral-small-2:24b",
        messages=messages
    )
    return response["message"]["content"].strip()





@app.post("/process/")
async def process_audio(file: UploadFile = File(...)):

    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Transcribe audio using Whisper
    transcript = model.transcribe(tmp_path)["text"]


    # Generate summary using Ollama
    summary_prompt = (
        "Summarize the following meeting transcript:\n\n"
        f"{transcript}"
    )
    summary = call_ollama(summary_prompt)



    # Generate action items using Ollama    
    tasks_prompt = (
        "List the key action items from this meeting:\n\n"
        f"{transcript}"
    )
    action_items = call_ollama(tasks_prompt)



    return {
        "transcript": transcript.strip(),
        "summary": summary,
        "action_items": action_items
    }
