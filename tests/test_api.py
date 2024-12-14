import pytest
import timeit
import json
from main import get_stock_price, Scraper

real_stocks = [
    "MSFT", "AMZN", "NVDA", "WMT", "GOOG", "AAPL", "AMD", "BA", "TSLA", "UBER",
    "NFLX", "V", "F", "AAL", "HOOD"
]

invalid_stocks = ["dEl", "MSFFT", "AMZN1", "NVDA!", "WM_T", "FAKE", "CSGO"]


@pytest.mark.parametrize("symbol", real_stocks)
def test_api(symbol):
    price = get_stock_price(symbol)
    assert price > 1


def test_api_response_time():
    # TODO add sleep to prevent limiting
    number_of_runs = 20
    times = []
    while number_of_runs != 0:
        time = timeit.timeit(lambda: get_stock_price("AAPL"), number=1)
        times.append(time)
        number_of_runs -= 1

    with open("api_times.json", 'w') as f:
        json.dump(times, f, indent=4)
    
    assert True


def test_api_average_response_time():
    # this can also be used for simulating high traffic by setting the number_of_runs to something higher like 100. but i plan on adding a separate test for that using locust
    number_of_runs = 20
    time = timeit.timeit(lambda: get_stock_price("AAPL"),
                         number=number_of_runs)
    average_time = time / number_of_runs
    print(average_time)
    assert average_time > 0


# def test_api_invalid_inputs():
#     pass
