import streamlit as st
from trustify.services.opengateway import verify_identity_and_number

def verify_section():
    st.header("Verificación de identidad y número")

    phone = st.text_input("Número de teléfono (e.g. +34612345678)")
    name = st.text_input("Nombre completo")

    if st.button("Verificar"):
        if phone and name:
            with st.spinner("Consultando Open Gateway..."):
                result = verify_identity_and_number(phone, name)
                if result:
                    st.success("Verificación completada")
                    st.json(result)
                else:
                    st.error("No se pudo verificar.")
        else:
            st.warning("Introduce ambos campos para continuar.")
