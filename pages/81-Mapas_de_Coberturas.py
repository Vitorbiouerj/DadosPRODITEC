import streamlit as st
import streamlit.components.v1 as components

# --- Interface Streamlit ---
st.title("📊 Mapas Coropléticos do PRODITEC")

# 🔹 Adicionando um parágrafo explicativo
st.markdown(
    """
    Os mapas abaixo representam o **percentual de escolas atendidas** pelo PRODITEC, considerando o número total de escolas em cada localidade e o número de participantes inscritos no programa.  
    A intensidade da cor no mapa indica a proporção de escolas atendidas: regiões mais escuras representam maior cobertura do PRODITEC, enquanto as mais claras indicam menor participação relativa.
    """
)


# Função para exibir um arquivo HTML corretamente
def exibir_html(arquivo_html, titulo):
    """Lê um arquivo HTML e exibe seu conteúdo no Streamlit corretamente."""
    try:
        with open(arquivo_html, "r", encoding="utf-8") as f:
            html_content = f.read()

        st.subheader(titulo)  # Adiciona um título para cada mapa
        components.html(html_content, height=600, scrolling=True)  # Renderiza o HTML corretamente

    except FileNotFoundError:
        st.error(f"❌ Arquivo não encontrado: {arquivo_html}")


# 🔹 Exibir os mapas corretamente
exibir_html("mapa_coropletico_2024_porcentagem.html", "🗺️ Percentual de Escolas Atendidas - 2024/2")
exibir_html("mapa_coropletico_2025_porcentagem.html", "🗺️ Percentual de Escolas Atendidas - 2025/1")
exibir_html("mapa_coropletico_total_porcentagem.html", "🗺️ Percentual de Escolas Atendidas - Total")
