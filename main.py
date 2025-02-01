import streamlit as st



from graph import graph_compiled
import random
import json
import base64
from io import BytesIO
import requests
import streamlit as st
from PIL import Image



from state import State

from config import config



def response_ai(prompt):


    user_input =  prompt


    output = graph_compiled.invoke({"messages": [user_input]},config=config)

    ai_message = output['messages'][-1].content
    

    return ai_message

st.title("💬 Agente LangGraph")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Olá, como posso te ajudar?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg = response_ai(prompt)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)