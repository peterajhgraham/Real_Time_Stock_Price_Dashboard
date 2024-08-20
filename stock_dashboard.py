import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pytz
import ta

# Fetch stock data based on ticker, period, & interval
def fetch_stock_data(ticker, period, interval):
  end_date = datetime.now()
  if period == '1wk':
    start_date = end_date - timedelta(days=7)
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
  else:
    data = yf.download(ticker, start=start_date, interval=interval)
  return data

# Process data to ensure it is timezone aware with correct formatting
def process_data(data)
  if data.index.tzinfo is None:
    data.index = data.index.tz_localize('UTC')
  data.index = data.index.tz_convert('US/Eastern')
  data.reset_index(inplace=True)
  data.rename(columns={'Date': 'Datetime'}, inplace=True)
  return data

# In Progress...
  
