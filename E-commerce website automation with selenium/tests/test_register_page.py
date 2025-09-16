import pytest
import time
from pages.register_user import RegisterPage


@pytest.mark.usefixtures("init_driver")
class TestCase1:
    def test_register_page(self):
        register=RegisterPage(self.driver)
        register.verify_homepage_visible()
        
        register.new_user_signup("Rakesh","rakesh1234@gmail.com")
        register.enter_information()
        time.sleep(2)
        register.enter_password("Rakesh@123")
        time.sleep(2)
        register.date()
        time.sleep(2)
        register.month()
        register.year()
        register.new_sletter()
        time.sleep(2)
        register.enter_account_details("Rakesh","Goud","Wipro","KPHB COLONY","Telangana","Hyderabad","500072","6300527653")
        time.sleep(2)
        register.create_account()
        time.sleep(2)
        register.check_title_matches()
        time.sleep(2)
        register.delete_account()
        time.sleep(2)

    
        