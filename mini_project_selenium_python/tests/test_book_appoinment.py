from config.config import ConfigPage
from pages.book_appoinment import BookAppoinment
from selenium import webdriver
import pytest
import time


@pytest.mark.usefixtures("init_driver")
class TestAppoinmentPage:
    def test_book_appoinment(self):
        self.driver.get(ConfigPage.BASE_URL)
        bookappoinment=BookAppoinment(self.driver)
        bookappoinment.book_appoinment()
        time.sleep(2)
        bookappoinment.login("John Doe","ThisIsNotAPassword")
        time.sleep(2)
        bookappoinment.start_process()
        time.sleep(2)
        bookappoinment.choose_date()
        time.sleep(2)
        bookappoinment.add_comment("Please! conform my appoinment")
        time.sleep(2)
        bookappoinment.submit()
        time.sleep(2)
        bookappoinment.take_screen_shot()
        time.sleep(2)
        bookappoinment.back_home()
        time.sleep(2)
        