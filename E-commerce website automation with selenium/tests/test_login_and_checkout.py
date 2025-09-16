import pytest
from pages.login_and_checkout import LoginAndCheckout   # adjust path to your file

@pytest.mark.usefixtures("init_driver")
class TestCase16:

    def test_login_checkout_flow(self):
        page = LoginAndCheckout(self.driver)

        # Step 1: Verify homepage
        page.verify_homepage_visible()

        # Step 2: Login with existing user
        page.login("bairirakeshgoud9908@gmail.com", "Rakesh@123")

        # Step 3: Verify login success
        page.check_title_matches()

        # Step 4: Add products to cart
        page.click_products()
        page.move_to_element()
        page.add_product()
        page.click_cart()

        # Step 5: Proceed to checkout
        page.proceed_to_checkout()

        # Step 6: Add order message
        page.send_msg("Place order")

        # Step 7: Enter payment details
        page.card_details(
            name="Rakesh Goud",
            number="4111111111111111",   # standard VISA test number
            cvc="123",
            month="12",
            year="2026"
        )

        # Step 8: Verify order success
        page.order_success()
