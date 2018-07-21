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
        path = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY' \
               '&symbol={}&apikey=' + API_KEY
        path = path.format(symbol)
        try:
            r = requests.get(path)
            price = list(r.json()['Time Series (Daily)'].values())[0]['4. close']
            text += 'Current price of {} is: {}\n'.format(symbol, price)
        except:
            text += 'Stock symbol "{}" not found.\n'.format(symbol)
    response.message(text)
    return str(response)

if __name__ == "__main__":
    app.debug = True
    app.run()
