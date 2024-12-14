import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

API_KEY = os.getenv('FINNHUB_API_KEY')
FAKE_API_KEY = "topsecret"
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

# ---------- FINNHUB PART


def get_stock_price(symbol: str):
    response = requests.get(
        url=f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}")
    response.raise_for_status()
    print(response.status_code, response.text)
    data = response.json()

    # with open("stock_data.json", mode="a") as file:
    #     file.write(f"{data}")


# ---------- SELENIUM PART


class Scraper:

    driver = ''

    def setup(self):
        chrome_driver_path = "./chromedriver.exe"

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(
            options=options,
            service=Service(executable_path=chrome_driver_path))

    def scrap_stock_price(self, symbol):
        self.driver.get(f"https://finance.yahoo.com/quote/{symbol}/")

        # the relative xpath below isnt the most optimal but for some reason selenium would grab a diff html element compared to the one chrome dev tools would bring up
        price = self.driver.find_element(
            By.XPATH, "//div[@class='price yf-k4z9w']//section//span").text

        return price

    def teardown(self):
        self.driver.close()


# finnhub is handling invalid symbols gracefully
# also just noticed that symbol must be UPPER
# TODO make sure to add this to pytest
# get_stock_price("aapl")

scraper = Scraper()

scraper.setup()
scraper.scrap_stock_price("AAPL")
scraper.teardown()
