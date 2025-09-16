import pytest, time
from pages.negative_amount import NegativeAmount

@pytest.mark.usefixtures('setup')
class Test8:
    def test_case8(self):
        login_obj = NegativeAmount(self.driver)
        login_obj.click_signin()
        login_obj.login()
        self.driver.back()
        login_obj.verify_account_summary()
        time.sleep(2)
        login_obj.transfer_fund("2")
        login_obj.select("4")
        login_obj.enter_money('-5000',"transaction complete")