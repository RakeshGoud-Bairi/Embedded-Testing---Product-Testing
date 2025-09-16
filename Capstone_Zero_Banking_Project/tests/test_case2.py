import pytest
from pages.incorrect_details import IncorrectDetails

@pytest.mark.usefixtures('setup')
class Test2:
    def test_case2(self):
        login_obj = IncorrectDetails(self.driver)
        login_obj.click_signin()
        login_obj.login("usser","pass")
        login_obj.error_msg()
    