import pytest
import time
from pages.check_with_existing_details import ExistingUser


@pytest.mark.usefixtures("init_driver")
class TestCase5:
    def test_register_page(self):
        existing_user=ExistingUser(self.driver)
        existing_user.verify_homepage_visible()
        time.sleep(2)
        existing_user.check_existing_user("Rakesh","bairirakeshgoud9908@gmail.com")
        time.sleep(2)
        existing_user.verify_email_already_exist()
        time.sleep(2)
