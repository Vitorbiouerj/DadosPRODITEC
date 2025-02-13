import streamlit as st
import streamlit.components.v1 as components

# --- Interface Streamlit ---
st.title("🌍 Visualizador de Mapas do PRODITEC")

# 🔹 Adicionando um parágrafo explicativo
st.markdown(
    """
    Os mapas abaixo mostram a distribuição geográfica dos cursistas do PRODITEC em diferentes edições.
    Você pode visualizar os participantes de 2024/2, 2025/1 e o total acumulado.  
    Os pontos no mapa representam os municípios, e o tamanho dos marcadores indica a quantidade de cursistas em cada localidade.
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
exibir_html("mapa_2024_bolha_distribuição.html", "📍 Distribuição dos Cursistas - 2024/2")
exibir_html("mapa_2025_bolha_distribuição.html", "📍 Distribuição dos Cursistas - 2025/1")
exibir_html("mapa_total_bolha_distribuição.html", "📍 Distribuição dos Cursistas - Total")
