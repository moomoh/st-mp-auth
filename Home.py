import streamlit as st

from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit Multipage App! 👋")
st.write("Here you will experience Signin with Google. :white_check_mark:")

if "token" in st.session_state:
    if st.button("Logout"):
        switch_page("Logout")
else:
    if st.button("Login"):
        switch_page("Account")
