from base.base_page import BasePage
from config.config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

class DownloadStatement(BasePage):
    SIGNIN_BTN_LOCATOR = (By.XPATH, '//*[@id="signin_button"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="user_login"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="user_password"]')
    SIGNIN_BTN = (By.XPATH, '//*[@id="login_form"]/div[2]/input')
    ONLINE_LOCATOR=(By.XPATH,'//*[@id="onlineBankingMenu"]/div/strong')
    MOVE_TO_STATEMENT=(By.XPATH,'//*[@id="online_banking_features"]/div[2]/div[3]/p')
    ONLINE_STATEMENT=(By.XPATH,'//*[@id="online_statements_link"]')
    STATEMENT_LOCATOR=(By.XPATH,'//*[@id="os_2012"]/table/tbody/tr/td[1]/a')


    def click_signin(self):
        self.click_operation(self.SIGNIN_BTN_LOCATOR)

    def login(self):
        self.enter_text(self.LOGIN_FIELD, Config.USERNAME)
        self.enter_text(self.PASSWORD_FIELD, Config.PASSWORD)
        self.click_operation(self.SIGNIN_BTN)
        print('The user is successfully logged in.')

    def verify_account_summary(self):
        self.click_operation(self.ONLINE_LOCATOR)

    def move_to_element(self):
        self.mouse_hover(self.MOVE_TO_STATEMENT)
        self.click_operation(self.ONLINE_STATEMENT)

    def go_to_statement(self):
        
        self.click_operation(self.STATEMENT_LOCATOR)
        print("statement downloaded successfully")
