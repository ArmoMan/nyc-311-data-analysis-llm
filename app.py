import streamlit as st
from src.llm.agent import Agent

# https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
if "agent" not in st.session_state:
    st.session_state.agent = Agent()

st.title("NYC 311 Data Analysis")

with st.container():
    st.write("Enter your question about NYC 311 data below. The AI will answer using the available tools and data.")

    question = st.text_input("Enter your question here:")

    if st.button("ASK"):
        if question:
            response = st.session_state.agent.ask(question)
            st.write(response)