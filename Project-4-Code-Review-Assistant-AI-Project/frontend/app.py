import streamlit as st
import requests
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv() 
BACKEND_URL = os.getenv("BACKEND_URL")


st.title("Code Review Assistant (Devstral-Small-2:24B)")

code_input = st.text_area(
    "Paste your code here:",
    height=300
)

if st.button("Get Review"):
    response = requests.post(
        f"{BACKEND_URL}/review/",
        data={"code": code_input}
    )
    review = response.json().get("review", "No feedback returned.")
    st.subheader("Review & Suggestions:")
    st.code(review)
