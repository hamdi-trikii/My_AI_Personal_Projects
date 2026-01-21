import streamlit as st
import requests
import os
from dotenv import load_dotenv



# Load environment variables from .env file
load_dotenv() 
BACKEND_URL = os.getenv("BACKEND_URL")

st.title("🎙️ AI Meeting Notes Generator")

audio_file = st.file_uploader(
    "Upload your meeting audio (.mp3 or .wav)",
    type=["mp3", "wav"]
)

if audio_file:
    st.audio(audio_file)

    if st.button("Generate Notes"):
        response = requests.post(
             f"{BACKEND_URL}/process/",
            files={"file": audio_file}
        )

        output = response.json()

        st.subheader("📝 Summary")
        st.write(output["summary"])

        st.subheader("✅ Action Items")
        st.write(output["action_items"])

        with st.expander("📄 Full Transcript"):
            st.text_area(
                "Transcript",
                value=output["transcript"],
                height=300
            )
