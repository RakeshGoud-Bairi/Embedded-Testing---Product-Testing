import pytest
import time
from pages.add_products import AddProducts


@pytest.mark.usefixtures("init_driver")
class TestCase12:
    def test_add_products(self):
        add_products=AddProducts(self.driver)
        add_products.verify_homepage_visible()
        add_products.click_products()
        add_products.move_to_element()
        add_products.add_product()
        add_products.click_cart()
        add_products.verify_products()
        add_products.product_prices()
        add_products.quantity()