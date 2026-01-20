from fastapi import FastAPI, UploadFile, File
import requests
import base64
import os
from ollama import Client
from dotenv import load_dotenv


load_dotenv()
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "https://ollama.com")

# Initialize Ollama client
client = Client(
    host=OLLAMA_HOST,
    headers={'Authorization': f'Bearer {OLLAMA_API_KEY}'}
)


app = FastAPI()

@app.post("/caption/")
async def caption_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")


    messages = [
        {
            "role": "user",
            "content": "Describe the image in one clear sentence.",
            "images": [image_base64],
        }
    ]



    response = client.chat(
        model="qwen3-vl:235b",
        messages=messages
    )



    return {"caption": response["message"]["content"].strip()}
