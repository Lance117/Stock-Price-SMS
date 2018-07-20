# Stock Price SMS

Sends stock prices via SMS.

Usage
-----

TODOs
-----
* Connect Twilio phone number to the app
* Task queue library to allow user to request prices of multiple stocks and set up notifications based on technical indicators

What it does
------

Currently, stock symbols sent via POST request are looked up using alphavantage API and the current stock price is returned. Goal: use twilio API to send alerts to user based on price movement/technical analysis or price threshold.
