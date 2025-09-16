import pytest
import time
from pages.verify_subscription_in_cart import CartSubscriptionPage


@pytest.mark.usefixtures("init_driver")
class TestCase11:
    def test_verify_subscription(self):
        verify_page=CartSubscriptionPage(self.driver)
        verify_page.verify_homepage_visible()
        verify_page.click()
        verify_page.scroll()
        time.sleep(2)
        verify_page.enter_email("bairirakeshgoud9908@gmail.com")
        time.sleep(1)
        verify_page.alert()
        time.sleep(2)