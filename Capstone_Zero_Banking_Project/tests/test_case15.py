import pytest
from pages.logout_page import LogoutPage

@pytest.mark.usefixtures('setup')
class Test15:
    def test_case15(self):
        logout_obj = LogoutPage(self.driver)
        logout_obj.click_signin()
        logout_obj.login()
        self.driver.back()
        logout_obj.logout()
