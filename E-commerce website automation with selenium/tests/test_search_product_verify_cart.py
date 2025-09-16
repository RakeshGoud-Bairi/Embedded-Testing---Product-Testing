import pytest
from pages.search_product_verify_cart import SearchProductVerify   # adjust import path if needed
@pytest.mark.usefixtures("init_driver")
class TestCase20:

    def test_search_add_and_remove_products(self):
        page = SearchProductVerify(self.driver)

        # Step 1: Verify homepage
        page.verify_homepage_visible()

        # Step 2: Click Products
        page.click_products()

        # Step 3: Search for product
        page.enter_product("Tshirt")

        # Step 4: Verify search results
        page.searched_products()

        # Step 5: Add products to cart
        page.add_products_to_cart()

        # Step 6: Login with existing user
        page.click_signup()
        page.fill_details("bairirakesh@gmail.com", "Rakesh@123")

        # Step 7: Go to cart
        page.click_cart()

        # Step 8: Remove all products
        page.remove_products()

        # Step 9: Verify empty cart message
        page.empty_cart()
