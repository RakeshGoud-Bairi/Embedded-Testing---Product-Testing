import pytest
import time
from pages.contact_us_page import ContactUs
import os


@pytest.mark.usefixtures("init_driver")
class TestCase6:
    def test_contactus_page(self):
        contact_us=ContactUs(self.driver)
        time.sleep(2)
        contact_us.verify_homepage_visible()
        time.sleep(2)
        contact_us.click_on_contactus()
        contact_us.fill_details("Rakesh","bairirakeshgoud9908@gmail.com","Keep your file","check the file")
        time.sleep(2)
        contact_us.add_path()
        time.sleep(2)
        contact_us.conform_alert()
        time.sleep(2)
        contact_us.success_msg()
        time.sleep(2)
        contact_us.return_home()
        time.sleep(2)
