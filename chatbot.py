from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st

# prompt template
prompt_temp = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful data science tutor. Please respond to the questions."),
        ("user", "Question: {question}")
    ]
)

#streamlit
st.title('LangChain Data Science Tutor')
input_text = st.text_input("Ask your data science question!")

#model
chat_model = Ollama(model="llama2")

#chain
chain = prompt_temp | chat_model

#display output/invoking
if input_text:
    st.write(chain.invoke({"question": input_text}))