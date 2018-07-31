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
        # RSI weekly, look-back period=10. RSI = 100-100/(1+RS).
        # RS=avg gain/avg loss over a period.
        # How to interpret: >70 indicates overbought, <30 reflects oversold
        # conditions. Useful for ranging market
        path2 = 'https://www.alphavantage.co/query?function=RSI' \
                '&symbol={}&interval=weekly&time_period=10&' \
                'series_type=close&apikey=' + API_KEY
        path2 = path2.format(symbol)
        try:
            r = requests.get(path)
            r2 = requests.get(path2)
            price = list(r.json()['Time Series (Daily)'].values())[0]['4. close']
            rsi_dict = r2.json()["Technical Analysis: RSI"]
            rsi = list(rsi_dict.values())[0]['RSI']
            rsi = float(rsi)
            recommend = 'HOLD'
            if rsi > 70:
                recommend = 'SELL'
            elif rsi < 30:
                recommend = 'BUY'
            text += 'Current price of {} is: {}\n' \
                    'RSI is {}. {} (non-trending stocks)\n'.format(symbol,
                        price, rsi, recommend)
        except:
            text += 'Stock symbol "{}" not found.\n'.format(symbol)
        
    response.message(text)
    return str(response)

if __name__ == "__main__":
    app.debug = True
    app.run()
