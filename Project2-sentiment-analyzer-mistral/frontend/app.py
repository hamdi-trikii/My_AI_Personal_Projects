import streamlit as st
import requests
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv() 
BACKEND_URL = os.getenv("BACKEND_URL")


st.title("Sentiment Analyzer (Mistral)")

text_input = st.text_area("Enter your sentence here:")

if st.button("Analyze"):
    response = requests.post(
        f"{BACKEND_URL}/analyze/",
        data={"text": text_input}
    )
    sentiment = response.json().get("sentiment", "Error")
    st.subheader("Predicted Sentiment:")
    st.write(sentiment)
