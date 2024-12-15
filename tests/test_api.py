import pytest
import timeit
import json
import requests
from main import get_stock_price, Scraper, API_KEY, FAKE_API_KEY

real_stocks = [
    "MSFT", "AMZN", "NVDA", "WMT", "GOOG", "AAPL", "AMD", "BA", "TSLA", "UBER",
    "NFLX", "V", "F", "AAL", "HOOD"
]

invalid_stocks = ["dEl", "MSFFT", "AMZN1", "NVDA!", "WM_T", "FAKE", "CSGO"]


@pytest.mark.parametrize("symbol", real_stocks)
def test_api(symbol):
    price = get_stock_price(symbol)
    assert price > 1


def test_api_invalid_key():
    with pytest.raises(requests.exceptions.HTTPError) as e:
        response = requests.get(
            url=
            f"https://finnhub.io/api/v1/quote?symbol=AAPL&token={FAKE_API_KEY}"
        )
        response.raise_for_status()


@pytest.mark.parametrize("symbol", real_stocks)
def test_api_response(symbol):
    response = requests.get(
        url=f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}")
    response.raise_for_status()
    code = response.status_code
    assert code < 400


def test_api_response_time():
    # TODO add sleep to prevent api limiting
    response_time_threshold = .3  # in seconds
    number_of_runs = 20
    times = []
    while number_of_runs != 0:
        time = timeit.timeit(lambda: get_stock_price("AAPL"), number=1)
        times.append(time)
        number_of_runs -= 1

    with open("api_times.json", 'w') as f:
        json.dump(times, f, indent=4)

    assert max(times) < response_time_threshold


def test_api_average_response_time():
    # this can also be used for simulating high traffic by setting the number_of_runs to something higher like 100. but i plan on adding a separate test for that using locust
    response_time_threshold = .3  # in seconds
    number_of_runs = 20
    time = timeit.timeit(lambda: get_stock_price("AAPL"),
                         number=number_of_runs)
    average_time = time / number_of_runs
    print(average_time)
    assert average_time < response_time_threshold


@pytest.mark.parametrize("symbol", invalid_stocks)
def test_api_invalid_inputs(symbol):
    # finnhub still returns a 200 code even if invalid inputs are provided. the only way to tell if the input was invalid is if the provided price is = 0. it is safe to assume most stocks wont be = $0
    price = get_stock_price(symbol)
    assert price == 0
