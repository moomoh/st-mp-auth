import streamlit as st
import os
import asyncio
import time
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
from httpx_oauth.clients.google import GoogleOAuth2
from dotenv import load_dotenv



async def write_authorization_url(client, redirect_uri):
    authorization_url = await client.get_authorization_url(
        redirect_uri,
        scope=["profile", "email"],
        extras_params={"access_type": "offline"},
    )
    return authorization_url


async def write_access_token(client, redirect_uri, code):
    token = await client.get_access_token(code, redirect_uri)
    return token


async def get_email(client, token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email


def main(user_id, user_email):
    st.write(f"You are now logged in as {user_email}!")
    c1, c2 = st.columns(2)
    if c1.button("To Main!"):
        switch_page("Main")
    if c2.button("To Home!"):
        switch_page("Home")



if "token" in st.session_state:
    main(user_id=st.session_state.user_id, user_email=st.session_state.user_email)
else:
   # os.getenv('OPENAI_API_KEY')
    #environ
    #environ
    #environ 
    #]
    #[
    load_dotenv('credits.env')
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URI")

    client = GoogleOAuth2(client_id, client_secret)
    authorization_url = asyncio.run(
        write_authorization_url(client=client, redirect_uri=redirect_uri)
    )

    try:
        code = st.experimental_get_query_params()["code"]
    except:
        # card(
        #     title="Login with Google",
        #     text="Click Me",
        #     image="https://icon-library.com/images/sign-in-with-google-icon/sign-in-with-google-icon-3.jpg",
        #     url=authorization_url,
        # )
        st.write(
            f"""<h1>
            Login with Google: <a target="_self"
            href="{authorization_url}">link</a></h1>""",
            unsafe_allow_html=True,
        )
        # st.button("butt")
        # st.markdown(
        #     """
        #     <style>
        #     .stButton>button{width: 400px;}
        #     </style>
        #     """,
        #     unsafe_allow_html=True,
        # )
    else:
        # Execute if there's no exception: verify token is correct?
        try:
            token = asyncio.run(
                write_access_token(client=client, redirect_uri=redirect_uri, code=code)
            )
        except:
            st.write(
                f"""<h1>
                This account is not allowed or page was refreshed.
                Please try again: <a target="_self"
                href="{authorization_url}">link</a></h1>""",
                unsafe_allow_html=True,
            )
        else:
            # Check if token has expired:
            if token.is_expired():
                st.write(
                    f"""<h1>
                Login session has ended,
                please <a target="_self" href="{authorization_url}">
                login</a> again.</h1>
                """
                )
            else:
                st.session_state.token = token
                user_id, user_email = asyncio.run(
                    get_email(client=client, token=token["access_token"])
                )
                st.session_state.user_id = user_id
                st.session_state.user_email = user_email
                main(
                    user_id=st.session_state.user_id,
                    user_email=st.session_state.user_email,
                )
                time.sleep(2)
                switch_page("Home")
