import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data/credit_data.csv')

st.markdown('# Credit Risk Analyzer')

user_input=st.sidebar.slider('Input Age:', 20, 70)

st.write(f'The user inputted {user_input}')

clicked=st.sidebar.button('Generate Chart')

fig, ax=plt.subplots()

if clicked: 
    df[df['age']==user_input]['amount'].hist(ax=ax)
    st.pyplot(fig)