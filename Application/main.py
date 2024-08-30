import os
import streamlit as st
from chat_utility import get_answer

working_directory = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title = "Chat with Doc",
    page_icon="📄",
    layout="centered"
)

st.title("Ayurvedic Home Remedies Bot 🌿")
st.subheader("Powered by gemma2:2b using Ollama")

user_query = st.text_input("Ask your question")

if st.button("Run"):
    answer = get_answer(user_query)
    st.success(answer)



