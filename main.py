import os
import json
import requests
import timeit
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

load_dotenv()

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
    # im jsoninfing the response text instead of fetching response.json because response.json for some reason is misformated.
    data = json.loads(response.text)
    return data['c']


# ---------- SELENIUM PART


class Scraper:

    driver = ''

    def setup_scraper(self):
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


# TODO make sure to add this to pytest
# get_stock_price("AAPL")

# scraper = Scraper()

# scraper.setup_scraper()
# scraper.scrap_stock_price("AAPL")
# scraper.teardown()

    