import streamlit as st

st.title("number converter :)")

num = st.text_input("please enter your number")
base = st.selectbox("selec the type", ["decimal", "binary", "hexa", "octa"])

try:
    if st.button("convert"):
        if base == "binary":
            num = int(num, 2)
        elif base == "hexa":
            num = int(num, 16)
        elif base == "octa":
            num = int(num, 8)
        elif base == "decimal":
            num = int(num)
            
        binary = bin(num)[2:]
        octadecimal = oct(num)[2:]
        hexadecimal = hex(num)[2:]
        
        st.info(f"binary:   {binary}")
        st.info(f"octadecimal:   {octadecimal}")
        st.info(f"hexadecimal:   {hexadecimal.upper()}")
        s
except Exception as e:
    st.error(f"error:   {e}")