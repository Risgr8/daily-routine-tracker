import streamlit as st # type: ignore
import streamlit_authenticator as stauth # type: ignore
import yaml
from yaml.loader import SafeLoader
import datetime

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)
init_creatine_amount = config["creatine"]["amount"]
creatine_date_refreshed = config["creatine"]["date_refreshed"]
days_to_refresh = (datetime.date.today() - creatine_date_refreshed).days
creatine_amount = max(0, init_creatine_amount-(5*days_to_refresh))

if st.button("add 5g"):
    creatine_amount = min(160, creatine_amount+5)
    config["creatine"]["amount"] = creatine_amount
    config["creatine"]["date_refreshed"] = datetime.date.today()
    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)
if st.button("remove 5g"):
    creatine_amount = max(0, creatine_amount-5)
    config["creatine"]["amount"] = creatine_amount
    config["creatine"]["date_refreshed"] = datetime.date.today()
    with open('config.yaml', 'w') as file:
        yaml.dump(config, file)
st.write("current creatine amount: " + str(creatine_amount))
