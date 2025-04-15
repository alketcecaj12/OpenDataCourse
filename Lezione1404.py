import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf


st.title('Check your Stocks!')
st.markdown('### Predict the trend of your stocks!')
tit_dict = {"GOOG":'Google', "AAPL":'Apple', "TSLA":'Tesla', "MSFT":'Microsoft'}

title = st.selectbox("Pick your title among Google, Apple, Tesla and Microsoft ", ["GOOG", "AAPL", "TSLA", "MSFT"])
st.write('You selected --> ', tit_dict[title])

ticker = yf.Ticker(title)
data = ticker.history(period = '5Y')

st.markdown('##### Today\'s price !')
st.write(data.tail(1))
st.markdown('#### Showing the stock as a time series !')

st.line_chart(data['Close'])

st.markdown('#### .. and its return in percentage during the last five years! Click on double arrow to expand!')

st.line_chart(data['Close'].pct_change()*100)

st.markdown('### The prediction for the next 4 weeks (20 working days)')


st.markdown('### The forecasting methods uses ARIMA')
st.markdown('### Predicted a change of : ')
change = (last_val-current_val) / last_val * 100
change = round(change, 2)

st.write("### % ", change)

st.write('.. at the end of the forecasting period!')