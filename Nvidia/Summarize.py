from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = init_chat_model("nvidia/llama-3.3-nemotron-super-49b-v1", model_provider="nvidia")

st.header('Reasearch Tool')

user_input=st.text_input('Enter your prompt')

if st.button('Summarize'):
    result=model.invoke(user_input)
    st.write(result.content)
