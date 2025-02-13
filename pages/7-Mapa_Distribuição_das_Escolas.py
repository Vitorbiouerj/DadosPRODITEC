import streamlit as st
from streamlit_folium import st_folium
import folium
import os

# Verificar se o arquivo do mapa existe
mapa_path = "meu_mapa.html"

if not os.path.exists(mapa_path):
    st.error("O arquivo 'meu_mapa.html' não foi encontrado. Execute o script de geração do mapa antes de visualizar.")
else:
    st.title("Mapa Interativo de Escolas no Brasil")
    st.write("Este mapa apresenta a distribuição das escolas no Brasil, com diferenciação por estados e municípios.")

    # Carregar o mapa HTML
    with open(mapa_path, "r", encoding="utf-8") as f:
        mapa_html = f.read()

    # Exibir o mapa no Streamlit
    st.components.v1.html(mapa_html, height=600, scrolling=True)
