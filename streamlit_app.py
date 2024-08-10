import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd

st.title('Stock Market Prediction')

st.info('Stock Market Prediction using NN')

with st.expander('Data'):
  st.write('**Raw Data**')
  df  = pd.read_csv('https://raw.githubusercontent.com/RoyR02/Stock-pred1/master/AAPL.csv',nrows= 10)
  df
csv = st.file_uploader("upload file", type={"csv"})
if csv is not None:
    df = pd.read_csv(csv)
# st.write(spectra_df)
#Input Data
# df = yf.download('AAPL', start='2010-01-01', end='2020-12-31')
df.head()

with st.expander('Graph'):
  st.line_chart(data = csv, x = Date , y = Close, x_label=Date, y_label = Price , color = Red, width=None, height=None, use_container_width=True)
