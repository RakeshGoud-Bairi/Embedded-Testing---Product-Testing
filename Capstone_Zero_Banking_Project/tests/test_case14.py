import pytest
import time
from pages.download_statement import DownloadStatement
@pytest.mark.usefixtures("setup")
class Test14:
    def test_successful_bill_payment(self):
        bill_payment = DownloadStatement(self.driver)
        bill_payment.click_signin()
        bill_payment.login()
        self.driver.back()
        bill_payment.verify_account_summary()
        bill_payment.move_to_element()
        bill_payment.go_to_statement()