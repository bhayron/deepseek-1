import streamlit as st
from datetime import datetime

# Configurações iniciais
st.title("Chat Bonito")
st.markdown("<h3>Seja bem-vindo ao nosso chat!</h3>", unsafe_allow_html=True)

# Estilização CSS
st.markdown("""
    <style>
    .message-container {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    .message-user {
        background-color: #f0f0f0;
        padding: 15px;
        border-radius: 10px 10px 0 10px;
    }
    .message-other {
        background-color: #fff;
        padding: 15px;
        border-radius: 10px 10px 10px 0;
    }
    .message-time {
        font-size: 0.8em;
        color: #666;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Armazenamento de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input de mensagem
col1, col2 = st.columns([3, 1])
with col1:
    name = st.text_input("Seu nome:", placeholder="Digite seu nome")
    message = st.text_area("Mensagem:", placeholder="Digite sua mensagem...", height=100)

if st.button("Enviar"):
    if name and message:
        new_message = {
            "name": name,
            "message": message,
            "time": datetime.now().strftime("%H:%M:%S")
        }
        st.session_state.messages.append(new_message)

# Exibição das mensagens
for msg in st.session_state.messages:
    with st.container():
        col_a, col_b = st.columns([3, 1])
        if msg["name"] == name:
            with col_a:
                st.markdown(f"<div class='message-container'><div class='message-user'>"
                            f"{msg['message']}</div><div class='message-time'>"
                            f"{msg['time']}</div></div>", unsafe_allow_html=True)
        else:
            with col_b:
                st.markdown(f"<div class='message-container'><div class='message-other'>"
                            f"{msg['name']}: {msg['message']}</div><div class='message-time'>"
                            f"{msg['time']}</div></div>", unsafe_allow_html=True)