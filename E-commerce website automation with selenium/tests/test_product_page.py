import pytest
import time
from pages.products_page import ProductsPage


@pytest.mark.usefixtures("init_driver")
class TestCase8:
    def test_product_page(self):
        product_page=ProductsPage(self.driver)
        product_page.verify_homepage_visible()
        product_page.click_products()
        time.sleep(2)
        product_page.check_all_products()
        time.sleep(2)
        product_page.click_view_product()
        time.sleep(2)
        product_page.verify_details()
        time.sleep(2)