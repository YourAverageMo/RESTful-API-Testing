from main import API_KEY
from locust import HttpUser, task, between
from .test_api import real_stocks
import random


class FinnhubUser(HttpUser):
    # with wait(1,2) api should never hit limits
    wait_time = between(1, 2)

    @task
    def get_stock_price(self):
        symbol = random.choice(real_stocks)

        # you can also randomize the endpoints to hit the whole api but on the free tier i basically only have 1 endpoint
        self.client.get(
            url=
            f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}")
