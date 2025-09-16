import pytest,time
from pages.validate_account_type import ValidateAccountType

@pytest.mark.usefixtures('setup')
class Test5:
    def test_case5(self):
        login_obj = ValidateAccountType(self.driver)
        login_obj.click_signin()
        login_obj.login()
        self.driver.back()
        login_obj.verify_account_summary()
        time.sleep(2)
        login_obj.verify_account_type()