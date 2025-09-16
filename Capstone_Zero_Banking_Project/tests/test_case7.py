import pytest, time
from pages.insufficent_money import InsufficentFundTransfer

@pytest.mark.usefixtures('setup')
class Test7:
    def test_case7(self):
        login_obj = InsufficentFundTransfer(self.driver)
        login_obj.click_signin()
        login_obj.login()
        self.driver.back()
        login_obj.verify_account_summary()
        time.sleep(2)
        login_obj.transfer_fund("2")
        login_obj.select("4")
        login_obj.enter_money('9999999999999999999999999999999999999999999',"transaction complete")