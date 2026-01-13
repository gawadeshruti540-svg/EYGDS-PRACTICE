import streamlit as st
st.title("make a simple calculator app")
num1=st.number_input("Enter first number:")
num2=st.number_input("Enter second number:")
st.selectbox("Select operation:",["Add","Subtract","Multiply","Divide"])
if st.button("Calculate"):
    if operation=="Add":
        result=num1+num2
        if operation=="Subtract":
            result=num1-num2
        if operation=="Multiply":
            result=num1*num2
        if operation=="Divide":
            result=num1/num2
    st.write("Result:")