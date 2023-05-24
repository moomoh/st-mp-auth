# Streamlit Multi-page App with Authentication
Streamlit multipage with authentication using Google Oauth2.

## Introduction
Streamlit is a very convenient framework for Data Scientists/ AI Engineers to quickly showcase their models to end users, without spending too much time developing necessary parts for a full web app.

Once you are ready with your model and feel the need to expose it to a larger audience, you can easily deploy Streamlit app that serves your model to a platform like HuggingFace, Streamlit, or Heroku etc. Authentication becomes a necessary feature if you don't want your app is exposed to any anonymous user in the Web, which may lead to uncontrollable uses of your computing resources or billale API (which means costing you money, a lot of it).

This repo based on the instruction I found in this awesome blog post [Implementing Google OAuth in Streamlt](https://towardsdatascience.com/implementing-google-oauth-in-streamlit-bb7c3be0082c). A few modifications have been made as follows:
+ Use Streamlit built-in SessionState, that is available at the creation time of this repo (instead of the custom-build class as in the original instruction).
+ Introduce Multi-page structure to the app
+ Use some features from streamlit-extras to facilitate the navivation within app

This structure separates all the Authentication logics to pages like Account and Logout, then allows logics for the actual app be implemented cleanly in the Main.py page.

Currently, the app only support Google Authentication as instructed by the original post, but you can also implement other authentication mechanism such as Azure, or email/password, etc. to suit yourt needs.


## Setups
### Google Firebase/Cloud project
+ Create a new project in your Google Firebase console (or use a current project if you prefer to do so).
+ Setting up Google OAuth2 service, following instructions from [1]
+ If the project is in Testing mode, make sure to add any email, that will be used to sign-in, to be a test user.

### Streamlit app
+ On a local device, create an environment, e.g. using Conda, and install necessary packages in requirements.txt
+ In the terminal, export the environment variables that are need in the app: 
  - GOOGLE_CLIENT_ID: from the Google project
  - GOOGLE_CLIENT_SECRET: from the Google project
  - REDIRECT_URI: "http://localhost:8501"
+ Run ```streamlit run Home.py```
+ Streamlit had been config to rerun after every file save.

### Deployment
+ Deploy to Streamlit Share or HuggingFace Space, following their corresponding instructions
+ Make sure to setup required dependencies, and protect your secrets properly (rather than harcoding into source code).
+ Change the REDIRECT_URI secret to your actual online app URI.

## Links
+ [1] [Implementing Google OAuth in Streamlit, by Duc Anh Bui](https://towardsdatascience.com/implementing-google-oauth-in-streamlit-bb7c3be0082c)
+ [streamlit-google-oauth repo](https://github.com/uiucanh/streamlit-google-oauth)
+ [Streamlit Multipage App](https://docs.streamlit.io/library/get-started/multipage-apps)
+ [Streamlit-extras gallery](https://extras.streamlit.app/)
