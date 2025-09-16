import pytest
from pages.verify_session_expiry import SessionExpiry

@pytest.mark.usefixtures('setup')
class Test16:
    def test_case16(self):
        logout_obj = SessionExpiry(self.driver)
        logout_obj.click_signin()
        logout_obj.login()
        self.driver.back()
        logout_obj.logout()
        self.driver.back()
