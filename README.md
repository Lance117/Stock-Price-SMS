# Stock Price SMS

Sends stock prices, buy/sell/hold recommendations, and trend strength via SMS. Purpose: make it easier to retrieve stock prices and recommendation by technical analysis. Useful if you don't have mobile data. Received help from Twilio's old tutorial: [link](https://www.twilio.com/blog/2016/06/check-stock-prices-with-python-and-twilio-sms.html)

<img width=360px src="https://raw.githubusercontent.com/LanceSanity/Stock-Price-SMS/master/screenshot1.png" />

Setup
-----
Install dependencies: `requests` (an HTTP client), `Flask` (Python microframework), `Twilio` helper library
```
pip3 install requests flask twilio
```

Get an AlphaVantage API key, write to file called "api_key.txt" (in the project's root directory)
```
https://www.alphavantage.co/support/#api-key
```

Get a Twilio number
```
https://www.twilio.com/try-twilio
```

Get a public URL to expose the app. To test, you can use `ngrok` to assign a public URL
```
ngrok http 5000
```

Configure your Twilio number to make an HTTP request when receiving an SMS
```
# Twilio Console > phone numbers > Messaging
# A MESSAGE COMES IN > webhook > copy over your public URL
```

Usage
-----
```
# python3 app.py
# to test: curl -d "Body={INSERT STOCK SYMBOL}" -X POST http://127.0.0.1:5000/sms
```

TODOs
-----
* Create alt solution: script that runs periodically, checking for "buy" signals based on technical indicators
* Task queue library to allow user to set up notifications, such as price target

What it does
------

Current: user requests stock price via POST request to [Alpha Vantage API](https://www.alphavantage.co/) and the app returns today's stock price, RSI for buy/sell/hold recommendation, and ADX for trend strength. User can request multiple stock prices in a single message. To get the response via text, configure a Twilio number to make HTTP request to your URL that exposes the app.

Future: task queue library for notifications, a script that runs periodically to send user timely alerts.
