import pytest
import time
from pages.test_cases_page import CheckTestCase

@pytest.mark.usefixtures("init_driver")
class TestCase7:
    def test_testcase_page(self):
        test_case=CheckTestCase(self.driver)
        test_case.verify_homepage_visible()
        time.sleep(2)
        test_case.click_testcase_btn()
        time.sleep(2)
        