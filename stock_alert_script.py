#!/usr/bin/env python3
"""Reads stock list from file, responds w/ text if there's a buy/sell alert"""

import csv
import sys


def get_stock_list(stocklist=""):
    """Opens file and returns list of stocks"""
    data = []
    with open(stocklist) as f:
        reader = csv.reader(f)
        for r in reader:
            data.extend(r)
    return data

if __name__ == "__main__":
    tickers = get_stock_list('stocklist.csv')
    for ticker in tickers:
        print(ticker)
