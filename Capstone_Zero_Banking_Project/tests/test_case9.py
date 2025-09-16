import pytest
from pages.success_bill_payment import SuccessfullBillPayment
@pytest.mark.usefixtures("setup")
class Test9:
    def test_successful_bill_payment(self):
        bill_payment = SuccessfullBillPayment(self.driver)
        bill_payment.click_signin()
        bill_payment.login()
        self.driver.back()
        bill_payment.verify_account_summary()
        bill_payment.pay_bill("500", "2025-09-05", "Electricity Bill")
        
