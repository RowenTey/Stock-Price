import streamlit as st 
import yfinance as yf
import datetime
import seaborn as sb
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Hack4Pan",
    page_icon="https://cdn-icons-png.flaticon.com/128/3094/3094918.png",
    initial_sidebar_state='collapsed'
)

def get_user_input():
    input = st.text_input('Enter a stock', 'SPY')
    return input

@st.cache
def fetch_chart_data(input):
    data = yf.download(input)
    return data

def display_chart(input, data_close):
    st.header(input)
    st.subheader('Interactive chart - Close')
    st.line_chart(data_close)
    
    
st.image("https://cdn.substack.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4b8647a-09e8-4576-95de-e622dcc38d72_1280x720.jpeg")
st.title("Welcome to the Stock App!")

# get user input (in sidebar)
st.header("Which stock would you like to see today?")
stock = get_user_input()

# fetch chart data
chart = fetch_chart_data(stock)
chart_close = chart.drop(['High','Low','Adj Close','Open','Volume'], axis = 1)

# display chart
display_chart(stock, chart_close)

# prediction date
st.sidebar.subheader('Choose a date to start predicting')
days_to_train = chart.index[-1] - datetime.timedelta(days=60)
default = days_to_train - datetime.timedelta(days=1)
prediction_date = st.sidebar.date_input("Start date", value=default, min_value=chart.index[0], max_value=days_to_train)

# fetch plot data
plotData = chart.drop(["Open", "High", "Low", "Adj Close"], axis = 1)

# plot static chart 
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

sb.set(rc={'axes.facecolor':'#0E1117', 'figure.facecolor':'#0E1117',
           'axes.labelcolor':'white', 'xtick.color':'white','ytick.color':'white',
           'axes.labelweight':'bold'})
sb.lineplot(data=plotData['Close'], ax=ax1, alpha=1.0, color='orange')
sb.lineplot(x=plotData.index, y=plotData['Volume'], data=plotData['Volume'], color='yellow', ax=ax2, alpha=0.6)

st.subheader("Static chart - Close & Volume")
st.pyplot(fig,use_container_width=True)

# footer          
st.write("By Kai Seong & Horstann for Hack4Pan 2022.")
