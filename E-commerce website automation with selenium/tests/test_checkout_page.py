import pytest
from pages.checkout_page import CheckOut  # adjust import path if needed

@pytest.mark.usefixtures("init_driver")
class TestCase14:
    def test_checkout_page(self):
        add = CheckOut(self.driver)
        add.verify_homepage_visible()
        add.click_products()
        add.move_to_element()
        add.add_product()
        add.click_cart()
        add.proceed_to_checkout()
        add.register()
        add.new_user_signup("Rakesh", "rakesh122@test.com")
        add.enter_information()
        add.enter_password("Test@123")
        add.date(6)
        add.month("August")
        add.year(2002)
        add.new_sletter()
        add.enter_account_details(
            firstname="Rakesh",
            lastname="Goud",
            company="TestCompany",
            address="Hyderabad",
            state="Telangana",
            city="Hyderabad",
            zipcode="500001",
            mobile="9876543210"
        )
        add.create_account()
        add.check_title_matches()
        add.go_to_cart()
        add.send_msg("Please deliver this product fast")
        add.card_details(
            name="Rakesh Goud",
            number="4111111111111111",
            cvc="123",
            month="12",
            year="2026"
        )
        add.order_success()
        add.locate_delete()
