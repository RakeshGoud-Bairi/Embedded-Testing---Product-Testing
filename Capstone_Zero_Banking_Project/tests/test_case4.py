import pytest
from pages.account_summary import AccountSummery

@pytest.mark.usefixtures('setup')
class Test4:
    def test_case4(self):
        login_obj = AccountSummery(self.driver)
        login_obj.click_signin()
        login_obj.login()
        self.driver.back()
        login_obj.verify_account_summary()

