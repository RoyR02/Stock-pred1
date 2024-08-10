import streamlit as st

st.title('Stock Market Prediction')

st.info('Stock Market Prediction using NN')

with st.expander('Data'):
  st.write('**Raw Data**')
  df  = pd.read_csv('https://github.com/RoyR02/Stock-pred1/blob/master/AAPL.csv')
  st.write('**Date**')
  x = df.drop('date', axis=1)


