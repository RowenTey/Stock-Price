# 📈 Stock Prediction App
*A web app that allows users to predict stock prices using LSTM and compare them to actual prices.* <br>
*View it [here](https://share.streamlit.io/rowentey/stock-price/main/app.py). Made by [@RowenTey](https://github.com/RowenTey) & [@Horstann](https://github.com/Horstann)*

#### Video Demo: https://www.youtube.com/watch?v=SKLymjKc8Ic

---

## ❓ Assignment

*Problem Statement*: Current LSTM price prediction models can be easily thrown off by black swan events akin to Covid-19.

*Our Solution*: We hypothesise that black swan events are characterised by sudden spikes in trading volume. For example, when there is rapid buying or selling in a short amount of time. Our app allows students, professionals and enthusiasts alike to study the relationship between trade volume and the accuracy of LSTM predictions relative to actual prices.

## 🧪 Tech 

This website is fully coded with Python. We utilised the `Streamlit` module as our web app's framework, given its simplicity and effectiveness in visualising data.

The `Matplotlib` library was also used to visualise our data and construct our time series charts.

Our stock price prediction model is LSTM, built using Data Science and Machine Learning libraries like `Numpy`, `Pandas`, `Keras` and `Tensorflow`.

As for our stock price data, we extracted it via the `yfinance` API.

## 📁 Organisation

- [.streamlit/](https://github.com/Horstann/Stock-Prediction-App/tree/main/.streamlit) contains the front-end configurations of our web app
- [app.py](https://github.com/Horstann/Stock-Prediction-App/blob/main/app.py) contains the code of our Streamlit framework, LSTM prediction model and data visualisation
- [requirements.txt](https://github.com/Horstann/Stock-Prediction-App/blob/main/requirements.txt) contains all the libraries and modules required to execute our web app, alongside their respective versions

## ⚙ How To Use
1. First, type in the **ticker** symbol you're looking for.  
2. Next, click the arrow icon on the top left corner. This opens up a sidebar. Select the date you 3. wish to start predicting the stock price from.  
4. Give a moment for the model to process your input.  
5. And that's it! The prediction will appear magically before your eyes. It's that **easy**!
