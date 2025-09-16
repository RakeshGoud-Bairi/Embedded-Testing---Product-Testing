from base.base_page import BasePage
from config.config import Config
from selenium.webdriver.common.by import By

class LogoutPage(BasePage):
    SIGNIN_BTN_LOCATOR = (By.XPATH, '//*[@id="signin_button"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="user_login"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="user_password"]')
    SIGNIN_BTN = (By.XPATH, '//*[@id="login_form"]/div[2]/input')
    LOGIN_LOCATOR=(By.XPATH,'//*[@id="settingsBox"]/ul/li[3]/a')
    LOGOUT_LOCATOR=(By.XPATH,'//*[@id="logout_link"]')

    def click_signin(self):
        self.click_operation(self.SIGNIN_BTN_LOCATOR)

    def login(self):
        self.enter_text(self.LOGIN_FIELD, Config.USERNAME)
        self.enter_text(self.PASSWORD_FIELD, Config.PASSWORD)
        self.click_operation(self.SIGNIN_BTN)
        print('The user is successfully logged in.')

    def logout(self):
        self.click_operation(self.LOGIN_LOCATOR)
        self.click_operation(self.LOGOUT_LOCATOR)
        print("logged out successfully")