# Stock Price SMS

Sends stock prices, buy/sell/hold recommendations, and trend strength via SMS.

<img width=360px src="https://raw.githubusercontent.com/LanceSanity/Stock-Price-SMS/master/screenshot1.png" />

Usage
-----
```
# install flask, requests, twilio libraries [pip3 install requests flask twilio], get Twilio number (if you want the info texted to you)
>> Alpha Vantage API key
# TODOs...
# ./app.py, to test: curl -d "Body={INSERT STOCK SYMBOL}" -X POST http://127.0.0.1:5000/sms
# to setup text response w/ Twilio: expose Python app w/ a public URL, configure number to make HTTP request to 
>> your URL
```

TODOs
-----
* Create alt solution: script that runs periodically, checking for "buy" signals based on technical indicators
* Task queue library to allow user to set up notifications, such as price target

What it does
------

Current: user requests stock price via POST request to [Alpha Vantage API](https://www.alphavantage.co/) and the app returns today's stock price, RSI for buy/sell/hold recommendation, and ADX for trend strength. User can request multiple stock prices in a single message. To get the response via text, configure a Twilio number to make HTTP request to your URL that exposes the app.

Future: task queue library for notifications, a script that runs periodically to send user timely alerts.
