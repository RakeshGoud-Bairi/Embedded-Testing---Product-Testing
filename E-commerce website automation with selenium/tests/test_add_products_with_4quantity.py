import pytest
import time
from pages.add_product_with_4quantity import Add4Products


@pytest.mark.usefixtures("init_driver")
class TestCase13:
    def test_add_products(self):
        add_product=Add4Products(self.driver)
        add_product.verify_homepage_visible()
        add_product.click_products()
        add_product.move_to_element()
        add_product.view_details()
        add_product.quantity(4)
        add_product.add_to_cart()
        add_product.product_details()