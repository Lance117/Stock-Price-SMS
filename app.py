#!/usr/bin/env python3

import requests

from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)

API_KEY = 'EMM4D55C3NQAPPS9'

@app.route('/sms', methods=['POST'])
def sms():
    tickers = request.values.get('Body')
    tickers = tickers.split()
    text = ''
    response = MessagingResponse()
    for symbol in tickers:
        # Get current price
        path = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY' \
               '&symbol={}&apikey=' + API_KEY
        path = path.format(symbol)
        # RSI (or some other technical indicator)
        path2 = 'https://www.alphavantage.co/query?function=RSI' \
                '&symbol={}&interval=weekly&time_period=60&' \
                'series_type=close&apikey=' + API_KEY
        path2 = path2.format(symbol)
        try:
            r = requests.get(path)
            r2 = requests.get(path2)
            price = list(r.json()['Time Series (Daily)'].values())[0]['4. close']
            rsi_dict = r2.json()["Technical Analysis: RSI"]
            rsi = list(rsi_dict.values())[0]['RSI']
            text += 'Current price of {} is: {}\n' \
                    'RSI is {}\n'.format(symbol, price, rsi)
        except:
            text += 'Stock symbol "{}" not found.\n'.format(symbol)
        
    response.message(text)
    return str(response)

if __name__ == "__main__":
    app.debug = True
    app.run()
