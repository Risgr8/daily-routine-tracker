import streamlit as st

def get_currently_tracked():
    #select * from 
    return None

st.title('Configure tracking options')

if st.button('Add'):
    input_type = st.radio('Input Type', ('Checkbox', 'Number'))

if st.button('Remove'):
    currently_tracked = get_currently_tracked()
    choices = st.selectbox('What would you like to remove?', currently_tracked)