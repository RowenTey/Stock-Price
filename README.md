# [Stock-Price-Predictor](https://share.streamlit.io/rowentey/stock-price/main/app.py)
*A stock web app that allows users to see stock charts and stock price predictions using machine learning.*
---

This website is fully coded with Python, utilising the `Streamlit` module to structure our web app.  

The `Matplotlib` library was also used to visualize our data and construct our charts.

Our stock price prediction model is LSTM, built using Data Science and Machine Learning libraries like `Numpy`, `Pandas`, `Keras` and `Tensorflow`.  

Problem Statement: Current LSTM price prediction models can be easily thrown off by black swan events like Covid-19.

Our Solution: We hypothesise that black swan events are characterised by sudden spikes in trading volume. For example, when there is rapid buying or selling in a short amount of time. Our app allows students, professioals and enthusiasts alike to study the relationship between trade volume and the accuracy of LSTM predictions relative to actual prices.

First, type in the ticker symbol you're looking for.
Next, click on the sidebar to select the date you wish to start predicting the stock price from.
Give a moment for the model to process your input.
And that's it! The prediction will appear magically before your eyes. It's that easy!
