#!/usr/bin/env python3
"""App uses twilio API to respond to user query via text"""


import requests

from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)

API_KEY = read_api_key('/')
url = 'https://www.alphavantage.co/query?'

@app.route('/sms', methods=['POST'])
def sms():
    """Method sends stock price info via sms"""
    tickers = request.values.get('Body')
    tickers = tickers.split()
    
    # interval for technical indicators
    interval = 'weekly'
    
    response = MessagingResponse()
    for symbol in tickers:
        # Save symbol to file
        write_to_file(symbol)

        # Current price payload
        price_payload = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': symbol,
            'apikey': API_KEY
        }

        # RSI weekly, look-back period=10
        # https://www.investopedia.com/terms/r/rsi.asp
        # useful for ranging market
        rsi_payload = {
            'function': 'RSI',
            'symbol': symbol,
            'time_period': '10',
            'series_type': 'close',
            'apikey': API_KEY
        }

        # ADX: trend strength indicator
        # https://www.investopedia.com/articles/trading/07/adx-trend-indicator.asp
        adx_payload = {
            'function': 'ADX',
            'symbol': symbol,
            'interval': interval,
            'time_period': '60',
            'apikey': API_KEY
        }

        # Create message
        try:
            text = create_msg(price_payload, rsi_payload, adx_payload)
        except:
            text = 'Stock symbol "${}" not found.\n'.format(symbol)
        
    response.message(text)
    return str(response)

def create_msg(price_payload, rsi_payload, adx_payload):
    """Returns message to send."""
    text = ''
    r = requests.get(url, params=price_payload)
    r2 = requests.get(url, params=rsi_payload)
    r3 = requests.get(url, params=adx_payload)
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

def write_to_file(ticker):
    """Saves ticker in file"""
    with open('stocklist.csv', a) as f:
        f.write(ticker + '\n')

def read_api_key(filepath):
    """Read API key from file."""
    with open('api_key.txt', 'r') as f:
        return f.read().replace('\n', '')


if __name__ == "__main__":
    app.debug = True
    app.run()
