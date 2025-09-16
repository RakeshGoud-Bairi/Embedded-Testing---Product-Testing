from base.base_page import BasePage
from config.config import Config
from selenium.webdriver.common.by import By

class AccountSummery(BasePage):
    SIGNIN_BTN_LOCATOR = (By.XPATH, '//*[@id="signin_button"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="user_login"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="user_password"]')
    SIGNIN_BTN = (By.XPATH, '//*[@id="login_form"]/div[2]/input')
    ONLINE_LOCATOR=(By.XPATH,'//*[@id="onlineBankingMenu"]/div/strong')
    ACCOUNT_LOCATOR=(By.XPATH,'//*[@id="account_summary_link"]')

    def click_signin(self):
        self.click_operation(self.SIGNIN_BTN_LOCATOR)

    def login(self):
        self.enter_text(self.LOGIN_FIELD, Config.USERNAME)
        self.enter_text(self.PASSWORD_FIELD, Config.PASSWORD)
        self.click_operation(self.SIGNIN_BTN)
        print('The user is successfully logged in.')

    def verify_account_summary(self):
        self.click_operation(self.ONLINE_LOCATOR)
        text=self.find_web_element(self.ACCOUNT_LOCATOR).text
        assert text=="Account Summary"
        print(f"{text} visible successfully")