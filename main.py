import os
import json
import requests

API_KEY = os.getenv('FINNHUB_API_KEY')
'''
Finnhub response key

c: Current price
d: Change
dp: Percent change
h: High price of the day
l: Low price of the day
o: Open price of the day
pc: Previous close price
'''


def get_stock_price(symbol: str):
    response = requests.get(
        url=f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}")
    response.raise_for_status()
    data = response.json()

    with open("stock_data.json", mode="a") as file:
        file.write(f"{data}")


# finnhub is handling invalid symbols gracefully
# also just noticed that symbol must be UPPER
# TODO make sure to add this to pytest
get_stock_price("aapl")
