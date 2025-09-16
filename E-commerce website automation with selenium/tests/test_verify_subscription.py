import pytest
import time
from pages.verify_subscription import SubscriptionPage


@pytest.mark.usefixtures("init_driver")
class TestCase10:
    def test_verify_subscription(self):
        verify_page=SubscriptionPage(self.driver)
        verify_page.verify_homepage_visible()
        verify_page.scroll()
        time.sleep(2)
        verify_page.enter_email("bairirakeshgoud9908@gmail.com")
        time.sleep(1)
        verify_page.alert()
        time.sleep(2)