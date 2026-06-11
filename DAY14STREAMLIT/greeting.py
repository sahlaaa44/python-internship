import streamlit as st

st.title("greeting app")

#create a session
if "name" not in st.session_state:
    st.session_state.name = " "

#text input
name = st.text_input("enter name")

#button
if st.button("greet"):
    st.session_state.name = name

if st.session_state.name:
    st.success(f"hello,{st.session_state.name}")   