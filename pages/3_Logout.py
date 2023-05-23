import streamlit as st
from streamlit_extras.switch_page_button import switch_page


if "token" in st.session_state:
    st.write("Are you sure to log out?")
    if st.button("Sure, log out!"):
        for key in ["token", "user_id", "user_email"]:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()
        switch_page("Home")
else:
    st.write("You are not logged in yet.")
    if st.button("Back to Home"):
        switch_page("Home")
