import streamlit as st
from datetime import date
import yfinance as yf

# Define start date and today's date
START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# App title
st.title("Simplified Stock Market App")

# Sidebar for stock selection
stocks = ("AAPL", "GOOG", "MSFT", "TSLA", "AMZN")
selected_stock = st.selectbox("Select dataset", stocks)

# Load stock data
@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

# Load and display the data
data_load_state = st.text("Loading data...")
data = load_data(selected_stock)
data_load_state.text("Loading data...done!")

# Display the raw data
st.subheader('Raw data')
st.write(data.head())  # Show only the first few rows

# Simple plot of the closing prices
st.subheader('Closing Price')
st.line_chart(data['Close'])
