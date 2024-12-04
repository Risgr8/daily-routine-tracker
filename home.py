import streamlit as st # type: ignore
import streamlit_authenticator as stauth # type: ignore
import yaml
from yaml.loader import SafeLoader

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    path='./config.yaml'
)

if "authentication_status" not in st.session_state:
    st.session_state["authentication_status"] = None

if st.session_state["authentication_status"] is None:
    authentication_status = None
    if authenticator.login():
        name, authentication_status, username = authenticator.login()

    if authentication_status:
        st.session_state["authentication_status"] = True
        st.session_state["name"] = name
        st.session_state["username"] = username
    elif authentication_status is False:
        st.warning("Username/password is incorrect")
    elif authentication_status is None:
        st.warning("Please enter your username and password")

if st.session_state["authentication_status"]:
    st.sidebar.title(f"Welcome {st.session_state['name']}")
