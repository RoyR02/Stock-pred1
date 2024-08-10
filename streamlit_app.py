import streamlit as st
import pandas as pd

st.title('Stock Market Prediction')

st.info('Stock Market Prediction using NN')

with st.expander('Data'):
  st.write('**Raw Data**')
  df  = pd.read_csv('https://raw.githubusercontent.com/RoyR02/Stock-pred1/master/AAPL.csv')
  df


