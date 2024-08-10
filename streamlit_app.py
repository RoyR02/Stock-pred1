!pip install sklearn
import streamlit as st
import pandas as pd
import math
import numpy as np
import pandas as pd
import re
import json
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
import time
from keras.utils import plot_model

st.title('Stock Market Prediction')

st.info('Stock Market Prediction using NN')

with st.expander('Data'):
  st.write('**Raw Data**')
  df  = pd.read_csv('https://raw.githubusercontent.com/RoyR02/Stock-pred1/master/AAPL.csv',nrows= 10)
  df
csv = st.file_uploader("upload file", type={"csv"})
if spectra is not None:
    df = pd.read_csv(spectra)
# st.write(spectra_df)
#Input Data
# df = yf.download('AAPL', start='2010-01-01', end='2020-12-31')
df.head()

plt.figure(figsize=(16,8))
plt.title('Closing Price History')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.show()
