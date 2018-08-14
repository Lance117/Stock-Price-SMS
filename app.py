#!/usr/bin/env python3
"""App uses twilio API to respond to user query via text"""


import requests

from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)

API_KEY = '{insert alphavantage API key here}'

@app.route('/sms', methods=['POST'])
def sms():
    """Method sends stock price info via sms"""
    tickers = request.values.get('Body')
    tickers = tickers.split()
    
    # interval for technical indicators
    interval = 'weekly'
    
    response = MessagingResponse()
    for symbol in tickers:
        # Get current price
        path = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY' \
               '&symbol={}&apikey={}'
        path = path.format(symbol, API_KEY)

        # RSI weekly, look-back period=10
        # https://www.investopedia.com/terms/r/rsi.asp
        # useful for ranging market
        path2 = 'https://www.alphavantage.co/query?function=RSI' \
                '&symbol={}&interval={}&time_period=10&' \
                'series_type=close&apikey={}'
        path2 = path2.format(symbol, interval, API_KEY)

        # ADX: trend strength indicator
        # https://www.investopedia.com/articles/trading/07/adx-trend-indicator.asp
        path3 = 'https://www.alphavantage.co/query?function=ADX' \
                '&symbol={}&interval={}&time_period=60&apikey={}'
        path3 = path3.format(symbol, interval, API_KEY)

        # Create message
        try:
            text = create_msg(path, path2, path3)
        except:
            text = 'Stock symbol "${}" not found.\n'.format(symbol)
        
    response.message(text)
    return str(response)

def create_msg(price_json, rsi_json, adx_json):
    """Returns message to send."""
    text = ''
    r = requests.get(path)
    r2 = requests.get(path2)
    r3 = requests.get(path3)
    price = list(r.json()['Time Series (Daily)'].values())[0]['4. close']
    rsi_dict = r2.json()["Technical Analysis: RSI"]
    rsi = list(rsi_dict.values())[0]['RSI']
    rsi = float(rsi)
    adx = list(r3.json()['Technical Analysis: ADX'].values())[0]['ADX']
    adx = float(adx)
    recommend = 'HOLD'
    strength = ''
    if rsi > 70:
        recommend = 'SELL'
    elif rsi < 30:
        recommend = 'BUY'
    if adx < 25:
        strength = 'weak trend'
    elif adx < 50:
        strength = 'strong trend'
    elif adx < 75:
        strength = 'very strong trend'
    elif adx <= 100:
        strength = 'extremely strong trend'
    text += 'Current price of {} is: {}\n'.format(symbol, price)
    text += 'RSI is {}. {} (non-trending stocks)\n'.format(rsi, recommend)
    text += 'ADX is {}. Trend strength: {}\n'.format(adx, strength)
    return text

if __name__ == "__main__":
    app.debug = True
    app.run()
