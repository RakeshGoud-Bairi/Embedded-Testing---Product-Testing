import pytest
from pages.add_payee_missing_details import AddPayeeMissingDetails

@pytest.mark.usefixtures('setup')
class Test13:
    def test_case13(self):
        add_payee=AddPayeeMissingDetails(self.driver)
        add_payee.click_signin()
        add_payee.login()
        self.driver.back()
        add_payee.verify_account_summary()
        add_payee.add_new_payee("","","","")