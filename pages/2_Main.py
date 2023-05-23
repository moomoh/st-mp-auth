import streamlit as st
from streamlit_extras.switch_page_button import switch_page


if "token" not in st.session_state:
    switch_page("Home")
else:
    st.write("# Welcome to the main page! :white_check_mark:")
    st.write(
        """
        Implement the main logics of your application here,\n
        with all authentication codes delegated to Authentication & Logout pages.
    """
    )
    # if st.button("Login"):
    #     switch_page("Authentication")
