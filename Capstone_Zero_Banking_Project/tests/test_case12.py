import pytest
import time
from pages.add_newpayee import AddNewPayee
@pytest.mark.usefixtures("setup")
class Test12:
    def test_successful_bill_payment(self):
        bill_payment = AddNewPayee(self.driver)
        bill_payment.click_signin()
        bill_payment.login()
        self.driver.back()
        bill_payment.verify_account_summary()
        bill_payment.add_new_payee("Rakesh","Hyderabad,Telangana","5432167890","Electricity Bill Payment")
        
