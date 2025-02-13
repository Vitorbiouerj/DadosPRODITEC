import streamlit as st
import os

st.set_page_config(page_title="Heatmap 2025", layout="wide")
st.title("Heatmap 2025-1")

# Caminho para o arquivo HTML
html_file = "mapa_brasil_2025_1.html"

if os.path.exists(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    # Exibe o conteúdo HTML no Streamlit
    st.components.v1.html(html_content, height=600, scrolling=True)
else:
    st.error("Arquivo 'mapa_brasil_2025_1.html' não encontrado.")
