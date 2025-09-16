import pytest
from pages.empty_details import EmptyDetails

@pytest.mark.usefixtures('setup')
class Test3:
    def test_case3(self):
        login_obj = EmptyDetails(self.driver)
        login_obj.click_signin()
        login_obj.login()
        login_obj.error_msg()
    