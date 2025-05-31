import streamlit as st
from trustify_api.verification import verify_number, verify_identity
from trustify_api.analysis import analyze_audio
from trustify_api.ownership import generate_proof

st.title("Trustify — Verify Creative Trust")

st.subheader("🔍 Identity Verification")
phone = st.text_input("Phone number")
name = st.text_input("Full name")
if st.button("Verify Identity"):
    st.write(verify_number(phone))
    st.write(verify_identity(name))

st.subheader("🎧 Audio Analysis")
audio_file = st.file_uploader("Upload audio file")
if audio_file and st.button("Analyze Audio"):
    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())
    st.write(analyze_audio("temp_audio.wav"))
    st.write(generate_proof("temp_audio.wav"))
