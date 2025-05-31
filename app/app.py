import streamlit as st
from trustify.pages.verify import verify_section

st.set_page_config(page_title="Trustify", layout="centered")
st.title("Trustify 🔎")
st.caption("Verificación de propiedad intelectual y fiabilidad de artistas, autores y coders.")

verify_section()
