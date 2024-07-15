import os
import streamlit as st
#from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage


openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:

    # Create an OpenAI client.
    os.environ["OPENAI_API_KEY"]=openai_api_key
    
    st.title("🎈 langchain-streamlit-app")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("What is up")
    if prompt:

        st.session_state.messages.append({"role": "user","content":prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            chat_model = ChatOpenAI(
                model = "gpt-3.5-turbo"
            )
            messages = [HumanMessage(content=prompt)]
            respose = chat_model.invoke(messages)
            st.markdown(respose.content)
        st.session_state.messages.append({"role": "assistant","content":respose.content})
