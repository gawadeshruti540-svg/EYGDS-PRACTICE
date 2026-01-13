import streamlit as st
st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")
st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, " + name)
    