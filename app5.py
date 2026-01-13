import streamlit as st
st.title("Make a Calculator App")
st.write("This is a simple calculator app built with Streamlit.")
# Input fields for numbers
num1 = st.number_input("Enter first number:", value=0)
num2 = st.number_input("Enter second number:", value=0)
# Dropdown for operation selection
operation = st.selectbox("Select operation:", ("Add", "Subtract", "Multiply", "Divide"))
# Calculate button
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    st.write(f"The result is: {result}")