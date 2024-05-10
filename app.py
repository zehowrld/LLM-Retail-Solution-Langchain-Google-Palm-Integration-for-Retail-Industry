import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.set_page_config(page_title="Database Q/A App")
st.image("logo.jpg",width=100)
st.title("zeho T-shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)