import pytest
import time
from pages.logout_user import LogoutUser


@pytest.mark.usefixtures("init_driver")
class TestCase4:
    def test_logout_user(self):
        logout_user=LogoutUser(self.driver)
        logout_user.login("bairirakeshgoud9908@gmail.com","Rakesh@123")
        time.sleep(2)
        logout_user.check_title_matches()
        time.sleep(2)
        logout_user.logout()
        time.sleep(2)
        logout_user.navigate_login_page()
        time.sleep(2)