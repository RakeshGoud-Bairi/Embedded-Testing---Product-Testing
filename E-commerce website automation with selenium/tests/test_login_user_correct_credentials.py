import pytest
import time
from pages.login_user_correct_credentionals import LoginCorrectUser


@pytest.mark.usefixtures("init_driver")
class TestCase2:
    def test_login_user_correct_cradentials(self):
        correct_user=LoginCorrectUser(self.driver)
        correct_user.login("rakeshgoudbairi@gmail.com","Rakesh@123")
        time.sleep(2)
        correct_user.check_title_matches()
        time.sleep(2)