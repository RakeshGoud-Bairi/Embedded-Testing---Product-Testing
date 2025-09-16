from base.base_page import BasePage
from config.config import Config
from selenium.webdriver.common.by import By

class IncorrectDetails(BasePage):
    SIGNIN_BTN_LOCATOR = (By.XPATH, '//*[@id="signin_button"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="user_login"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="user_password"]')
    SIGNIN_BTN = (By.XPATH, '//*[@id="login_form"]/div[2]/input')
    ERROR_MSG=(By.XPATH,'//*[@id="login_form"]/div[1]')

    def click_signin(self):
        self.click_operation(self.SIGNIN_BTN_LOCATOR)

    def login(self,username,password):
        self.enter_text(self.LOGIN_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_operation(self.SIGNIN_BTN)

    def error_msg(self):
        text_msg=self.find_web_element(self.ERROR_MSG).text
        assert text_msg=="Login and/or password are wrong."
        print(f"{text_msg} visible successfully")