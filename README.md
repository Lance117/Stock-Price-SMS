# Stock Price SMS

Sends stock prices via SMS.

<img width=480px src="https://raw.githubusercontent.com/LanceSanity/Stock-Price-SMS/master/screenshot.png" />

Usage
-----
```
# install flask, request, twilio libraries
# TODOs...
# ./app.py and curl -d "Body=[INSERT STOCK SYMBOL]" -X POST http://127.0.0.1:5000/sms
```

TODOs
-----
* Allow user to request info for multiple stocks
* Add more useful info in response, such as buy/hold/sell recommendations
* Ask user for Alpha Vantage API key instead of using mine
* Create alt solution: script that runs periodically, checking for "buy" signals based on technical indicators
* Task queue library to allow user to set up notifications, such as price target

What it does
------

Current: user requests stock price via POST request to [Alpha Vantage API](https://www.alphavantage.co/) and the app returns today's stock price.

Future: user can request multiple stocks, more useful info than just stock price, task queue library for notifications, a script for personal use
