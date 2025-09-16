import pytest
from pages.pay_bill_without_amount import PayBillWithOutAmount

@pytest.mark.usefixtures('setup')
class Test11:
    def test_case11(self):
        pay_bill=PayBillWithOutAmount(self.driver)
        pay_bill.click_signin()
        pay_bill.login()
        self.driver.back()
        pay_bill.verify_account_summary()
        pay_bill.pay_bill("","2025-09-03","fund transfer")