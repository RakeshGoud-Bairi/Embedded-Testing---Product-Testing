import pytest
from pages.verify_address_details import VerifyAddress
@pytest.mark.usefixtures("init_driver")
class TestCase23:
    def test_verify_delivery_and_billing_address(self):
        # Create object of VerifyAddress POM
        verify = VerifyAddress(self.driver)

        # Step 1: Verify homepage
        verify.verify_homepage_visible()

        # Step 2: New user signup
        firstname = "Rakesh"
        lastname = "Goud"
        company = "TestCompany"
        address = "Hyderabad"
        state = "Telangana"
        city = "Hyderabad"
        zipcode = "500001"
        mobile = "9876543210"

        verify.new_user_signup(firstname, "rakesh1443@test.com")
        verify.enter_information()
        verify.enter_password("Test@123")
        verify.date(6)
        verify.month("August")
        verify.year(2002)
        verify.new_sletter()

        # Step 3: Enter account details
        verify.enter_account_details(firstname, lastname, company, address, state, city, zipcode, mobile)
        verify.create_account()

        # Step 4: Verify logged in
        verify.check_title_matches()

        # Step 5: Add products & go to checkout
        verify.click_product()
        verify.proceed_to_bill()

        # Step 6: Verify delivery & billing address
        # Need to assign details to object so `verify_address()` can check them
        verify.firstname = firstname
        verify.lastname = lastname
        verify.address = address
        verify.city = city
        verify.zipcode = zipcode
        verify.mobile = mobile
        verify.verify_address()

        # Step 7: Delete account
        verify.delete_account()
