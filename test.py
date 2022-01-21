import streamlit as st 
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="Hack4Pan",
    page_icon="https://cdn-icons-png.flaticon.com/128/3094/3094918.png",
)

st.title("Which stock would you like to see today?")

stock = st.text_input('Enter a stock', 'VOO')

chart = yf.download(str(stock))
chart_open = chart.drop(['High','Low','Adj Close','Volume','Close'], axis = 1)
chart_close = chart.drop(['High','Low','Adj Close','Volume','Open'], axis = 1)
chart_volume = chart.drop(['High','Low','Adj Close','Close','Open'], axis = 1)

st.header(stock)
st.subheader('Open')
st.line_chart(chart_open,use_container_width=True)
st.subheader('Close')
st.line_chart(chart_close,use_container_width=True)
st.subheader('Volume')
st.line_chart(chart_volume,use_container_width=True)
         
st.write("By Kai Seong & Horstann for Hack4Pan 2022.")