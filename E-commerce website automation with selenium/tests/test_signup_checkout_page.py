import pytest
from pages.signup_checkout import SignupCheckout   # adjust import path if needed

@pytest.mark.usefixtures("init_driver")
class TestCase15:

    def test_signup_checkout_flow(self):
        page = SignupCheckout(self.driver)

        # Step 1: Verify homepage
        page.verify_homepage_visible()

        # Step 2: Register new user
        page.new_user_signup("Rakesh", "rakesh_checkout@test.com")
        page.enter_information()
        page.enter_password("Test@123")
        page.date(6)
        page.month("August")
        page.year(2002)
        page.new_sletter()
        page.enter_account_details(
            firstname="Rakesh",
            lastname="Goud",
            company="QACompany",
            address="Hyderabad",
            state="Telangana",
            city="Hyderabad",
            zipcode="500001",
            mobile="9876543210"
        )
        page.create_account()

        # Step 3: Verify user is logged in
        page.check_title_matches()

        # Step 4: Add products to cart
        page.click_products()
        page.move_to_element()
        page.add_product()
        page.click_cart()

        # Step 5: Proceed to checkout
        page.proceed_to_checkout()

        # Step 6: Add order message
        page.send_msg("Please deliver ASAP")

        # Step 7: Enter payment details
        page.card_details(
            name="Rakesh Goud",
            number="4111111111111111",   # test Visa card number
            cvc="123",
            month="12",
            year="2026"
        )

        # Step 8: Verify order success
        page.order_success()

        # Step 9: Delete account
        page.locate_delete()
