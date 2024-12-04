import streamlit as st # type: ignore
import streamlit_authenticator as stauth # type: ignore
import yaml
from yaml.loader import SafeLoader

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)
init_creatine_amount = config["creatine"]["amount"]
creatine_date = config["creatine"]["date"]

creatine_amount = init_creatine_amount
st.write("current creatine amount: " + creatine_amount)
if st.button("add 5g"):
    config["creatine"]["amount"] = creatine_amount + 5
    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)
if st.button("remove 5g"):
    config["creatine"]["amount"] = creatine_amount + 5
    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)
