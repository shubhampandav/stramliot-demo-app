import streamlit as st
import requests
from bs4 import BeautifulSoup
import time 
import yfinance as yf
from datetime import datetime, timedelta

def fetch_live_price(ticker, exchange):
    url = f'https://www.google.com/finance/quote/{ticker}:{exchange}?hl=en'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    class1 = "YMlKec fxKbKc"
    price = float(soup.find(class_=class1).text.strip()[1:].replace(",", ""))
    return price

def fetch_previous_adj_close(ticker):
    end_date = datetime.now() - timedelta(days=1)  # Previous trading day
    start_date = end_date - timedelta(days=1)
    data = yf.download(ticker, start=start_date, end=end_date)
    previous_adj_close = data['Adj Close'].iloc[-1]
    return previous_adj_close

def main():
    st.title("Live Stock Price Tracker")

    ticker = st.text_input("Enter Ticker Symbol:")
    exchange = st.text_input("Enter Exchange:")
    
    if st.button("Track Price"):
        price_text = st.empty()  # Placeholder for displaying price
        
        while True:
            live_price = fetch_live_price(ticker, exchange)
            
            # Display the live price
            price_text.write(f"<p id='price-text'>Price: {live_price}</p>", unsafe_allow_html=True)
            
            time.sleep(1)

if __name__ == "__main__":
    main()
