import pytest, time
from pages.fund_transfer import FundTransfer

@pytest.mark.usefixtures('setup')
class Test6:
    def test_case6(self):
        login_obj = FundTransfer(self.driver)
        login_obj.click_signin()
        login_obj.login()
        self.driver.back()
        login_obj.verify_account_summary()
        time.sleep(2)
        login_obj.transfer_fund("2")
        login_obj.select("4")
        login_obj.enter_money('1000',"transaction complete")
