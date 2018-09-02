#!/usr/bin/env python3
"""Reads stock list from file, responds w/ text if there's a buy/sell alert"""

import csv
import sys

from twilio.rest import Client


def get_stock_list(stocklist=""):
    """Opens file and returns list of stocks"""
    with open(stocklist) as f:
        reader = csv.reader(f)
        data = [ticker[0] for ticker in reader]
    return data

def send_response(body):
    """Sends response from twilio no. to your number"""

    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = clients.messages.create(
                                    from_='+{YOUR TWILIO NO}',
                                    body=body,
                                    to='+{YOUR PHONE NO}'
                                )

    print(message.sid)

def create_alert(tickers):
    """Sends price alerts of given stock tickers"""
    pass

if __name__ == "__main__":
    tickers = get_stock_list('stocklist.csv')
    for ticker in tickers:
        print(ticker)
