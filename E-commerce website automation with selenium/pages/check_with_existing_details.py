from selenium.webdriver.common.by import By
from util.base_util import BasePage

class ExistingUser(BasePage):
    SIGIN_BTN=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
    NAME_LOCATOR=(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/input[2]")
    EMAIL_LOCATOR=(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/input[3]")
    SIGNUP_BTN=(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/button")
    ERROR_MSG=(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/p")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def check_existing_user(self,Name,Email):
        self.wait_for_clickable(self.SIGIN_BTN)
        self.enter_text(self.NAME_LOCATOR,Name)
        self.enter_text(self.EMAIL_LOCATOR,Email)
        self.wait_for_clickable(self.SIGNUP_BTN)

    def verify_email_already_exist(self):
        element=self.wait_for_visibility(self.ERROR_MSG).text
        assert "Email Address already exist!"==element
        print(f"{element} visible successfully")
