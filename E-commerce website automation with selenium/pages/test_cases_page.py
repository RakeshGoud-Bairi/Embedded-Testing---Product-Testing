from selenium.webdriver.common.by import By
from util.base_util import BasePage

class CheckTestCase(BasePage):
    TESTCASE_BTN=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")
    TESTCASE_HEADING=(By.XPATH,"//*[@id='form']/div/div[1]/div/h2/b")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def click_testcase_btn(self):
        self.wait_for_clickable(self.TESTCASE_BTN)
        element=self.wait_for_visibility(self.TESTCASE_HEADING).text
        print(f"{element} visible successfully")
