import pytest
from main import get_stock_price, Scraper, API_KEY, FAKE_API_KEY
from .test_api import real_stocks

@pytest.mark.parametrize("symbol", real_stocks)
class TestValidateAPI:
    def setup_method(self):
        # always preform these ops before testing
        self.scraper = Scraper()
        self.scraper.setup_scraper()

    def test_validate_api(self, symbol):
        price_tolerance = .3
        api_price = get_stock_price(symbol)
        real_price = self.scraper.scrap_stock_price(symbol)
        print(f"{api_price=}, {real_price=}")
        
        assert abs(api_price-real_price) <= price_tolerance

    def teardown_method(self):
        # always preform these ops after testing 
        self.scraper.teardown()