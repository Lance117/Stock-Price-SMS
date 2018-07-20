# Stock Price SMS

Sends stock prices via SMS.

Usage
-----
```
# install flask, request, twilio libraries
# TODOs...
# ./app.py and curl -d "Body=[INSERT STOCK SYMBOL]" -X POST http://://127.0.0.1:5000/sms
```

TODOs
-----
* Connect Twilio phone number to the app
* Ask user for Alpha Vantage API key instead of using mine
* Task queue library to allow user to request prices of multiple stocks and set up notifications

What it does
------

Current: user requests stock price via POST request to [Alpha Vantage API](https://www.alphavantage.co/) and the app returns today's stock price.

Future: app to notify user of stock price based on technical indicators.
