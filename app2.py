import streamlit as st
st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")
st.text_input("Enter your name:")
age=st.slider("Select your age:",1,100)
city=st.selectbox("choose your city:",["New York","Los Angeles","Chicago","Houston","Phoenix"])
if st.button("Submit"):
    st.write("Hello, " + name + "! You are " + str(age) + " years old and live in " + city + ".")   