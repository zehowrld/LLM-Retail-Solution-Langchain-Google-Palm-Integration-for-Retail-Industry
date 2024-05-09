import streamlit as st

st.set_page_config(page_title="Database Q/A App")

st.image("logo.jpg",width=100)
st.title("zeho T-shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question and submit:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)