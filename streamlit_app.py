import streamlit as st
from datetime import date

import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2010-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Pred App")

stocks = ("AAPL", "GOOG", "MSFT")
selected_stocks = st.selectbox("Select dataset",stocks)

n_years = st.slider("Years of pred: ",1, 5)
period = n_years * 365

def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    date.reset_index(inplace=True)
    return data

data_load_state = st.text("Loading......")
data = load_data(stocks)
data_load_state.text("Loading Data....done")
