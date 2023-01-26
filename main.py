from tempfile import NamedTemporaryFile

import streamlit as st

from src.model import sound_to_text, tiny_model

model = tiny_model

audio = st.file_uploader(
    "Upload an audio",
    type="mp3",
)

if audio:
    with NamedTemporaryFile(dir="output", suffix=".mp3") as f:
        f.write(audio.getbuffer())
        result_text = sound_to_text(model, f.name)
        st.write(result_text)
