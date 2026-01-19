from fastapi import FastAPI, Form
import requests

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

@app.post("/analyze/")
def analyze_sentiment(text: str = Form(...)):
    prompt = (
        "What is the sentiment of this text? "
        "Respond with Positive, Negative, or Neutral:\n\n"
        f"{text}"
    )
    # Call Ollama cloud model
    #code is from olmama documentation
    messages = [{"role": "user", "content": prompt}]

    response_text = ""

    for part in client.chat("mistral-large-3:675b", messages=messages, stream=True):
        response_text += part['message']['content']


    return {"sentiment": response_text.strip()}