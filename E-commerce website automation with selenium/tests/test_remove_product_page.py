import pytest
from pages.remove_products_from_cart import RemoveProducts

@pytest.mark.usefixtures("init_driver")
class TestCase17:
    def test_remove_product_from_cart(self):
        remove_product=RemoveProducts(self.driver)
        remove_product.verify_homepage_visible()
        remove_product.click_products()
        remove_product.move_to_element()
        remove_product.add_product()
        remove_product.click_cart()
        remove_product.remove_product()
        remove_product.cart_msg()