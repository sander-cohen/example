import streamlit as st

import numpy as np

st.write("""App to pick the largest number from three inputs""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    No1 = st.number_input("Enter First Number",min_value=0,step=1)
    No2 = st.number_input("Enter Second Number",min_value=0,step=1)
    No3 = st.number_input("Enter Third Number",min_value=0,step=1)
    features = np.array([No1,No2,No3])
    return features

df = user_input_features()
if (len(df)=3):
    st.subheader('Largest number is :')
    st.write(np.sort(df)[-1])
