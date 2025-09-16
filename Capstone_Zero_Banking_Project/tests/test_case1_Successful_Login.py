import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures('setup')
class Test1:
    def test_case1(self):
        login_obj = LoginPage(self.driver)
        login_obj.click_signin()
        login_obj.login()
        self.driver.back()
        title = self.driver.title
        assert 'Zero - Personal Banking - Loans - Credit Cards' in title
        print('The Account Summary page is displayed.')