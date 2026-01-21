from fastapi import FastAPI , Form
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


app=FastAPI()

@app.post("/review/")
def review_code(code: str = Form(...)):


    messages = [
        {
            "role": "user",
            "content": (
                "You are a senior developer. Please review the following code for bugs, "
                "improvements, and optimization tips:\n\n"
                f"{code}"
            )
        }
    ]

    response = client.chat(
        model="devstral-small-2:24b",
        messages=messages
    )

    return {"review": response["message"]["content"].strip()}