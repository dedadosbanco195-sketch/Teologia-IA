import streamlit as st
from agents.teologo import perguntar_teologia

st.set_page_config(
    page_title="Teologia IA",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Teologia IA")
st.write("Professor Bíblico Inteligente")

# Histórico
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# Input
pergunta = st.chat_input("Faça sua pergunta bíblica...")

if pergunta:

    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    resposta = perguntar_teologia(pergunta)

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta
    })

# Renderizar chat
for msg in st.session_state.mensagens:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
