import pytest
import time
from pages.incorrect_details import InCorrectDetails


@pytest.mark.usefixtures("init_driver")
class TestCase3:
    def test_incorrect_details(self):
        incorrect_details=InCorrectDetails(self.driver)
        incorrect_details.login("rakeshgoudbairi@gmail.com","rakesh@123")
        time.sleep(2)
        incorrect_details.error_msg()
        time.sleep(2)
