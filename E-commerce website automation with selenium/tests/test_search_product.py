import pytest
import time
from pages.search_product import SearchProductsPage


@pytest.mark.usefixtures("init_driver")
class TestCase9:
    def test_search_product(self):
        search_product=SearchProductsPage(self.driver)
        search_product.verify_homepage_visible()
        search_product.click_products()
        time.sleep(2)
        search_product.enter_product("Blue Top")
        time.sleep(2)
        search_product.searched_products()
        time.sleep(2)
        search_product.product_search_matches()
        time.sleep(2)