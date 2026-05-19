# ¿Qué tiene que hacer?

# Mostrar un título y descripción
# Permitir subir un PDF
# Cuando se sube, extraer el texto con pdf_reader.py
# Mandarlo a analizar con analyzer.py
# Mostrar el resultado

import streamlit as st
from pdf_reader import extraer_texto
from analyzer import analizar_documento

st.title("📄 Analizador de Documentos Legales")
st.write("Subí un contrato o documento legal en formato PDF y te lo explicamos en lenguaje simple.")

archivo = st.file_uploader("Subí tu PDF", type="pdf")

if archivo is not None:
    with st.spinner("Analizando el documento..."):
        texto = extraer_texto(archivo)
        resultado = analizar_documento(texto)
    st.markdown(resultado)


# Qué hace cada parte:

# st.title — el título de la página
# st.write — texto descriptivo
# st.file_uploader — el botón para subir el PDF, solo acepta PDFs
# if archivo is not None — espera a que el usuario suba algo
# st.spinner — muestra un loading mientras analiza
# extraer_texto — extrae el texto del PDF
# analizar_documento — lo manda a Gemini
# st.markdown — muestra el resultado con formato (los ## y emojis del prompt se ven bien)