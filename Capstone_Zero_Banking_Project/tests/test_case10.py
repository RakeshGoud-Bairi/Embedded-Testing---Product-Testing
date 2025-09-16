import pytest
from pages.future_bill_payment import FutureBillPayment
@pytest.mark.usefixtures("setup")
class Test9:
    def test_successful_bill_payment(self):
        bill_payment = FutureBillPayment(self.driver)
        bill_payment.click_signin()
        bill_payment.login()
        self.driver.back()
        bill_payment.verify_account_summary()
        bill_payment.pay_bill("5000", "2025-09-30", "Credit card bill")