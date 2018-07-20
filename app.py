import requests

from flask import Flask, request
from datetime import date
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)

API_KEY = 'EMM4D55C3NQAPPS9'

@app.route('/sms', methods=['POST'])
def sms():
    today = str(date.today())
    symbol = request.values.get('Body')
    path = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY' \
           '&symbol={}&apikey=' + API_KEY
    path = path.format(symbol)
    response = MessagingResponse()
    try:
        r = requests.get(path)
        price = r.json()['Time Series (Daily)'][today]['4. close']
        response.message('Current price of {} is: {}'.format(symbol, price))
    except:
        response.message('Stock symbol "{}" not found.'.format(symbol))
    return str(response)

if __name__ == "__main__":
    app.debug = True
    app.run()
