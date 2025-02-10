import streamlit as st
from langchain_ollama import ChatOllama

llm = ChatOllama(model="deepseek-r1:1.5b",
                 base_url="http://localhost:11434")

st.set_page_config(page_title="Chat DeepSeek", layout="centered")
st.title("Teste com DeepSeek")

in_message = st.chat_input("Envie sua dúvida:")
if in_message:
    chat = st.chat_message("human")
    chat.markdown(in_message)
    response = llm.invoke(in_message)
    chat = st.chat_message("ai")
    chat.markdown(response.content)