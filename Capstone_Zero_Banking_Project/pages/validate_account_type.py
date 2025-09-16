from base.base_page import BasePage
from config.config import Config
from selenium.webdriver.common.by import By

class ValidateAccountType(BasePage):
    SIGNIN_BTN_LOCATOR = (By.XPATH, '//*[@id="signin_button"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="user_login"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="user_password"]')
    SIGNIN_BTN = (By.XPATH, '//*[@id="login_form"]/div[2]/input')
    ONLINE_LOCATOR=(By.XPATH,'//*[@id="onlineBankingMenu"]/div')
    ACCOUNT_LOCATOR=(By.XPATH,'//*[@id="account_summary_link"]')
    CASH_LOCATOR=(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/h2[1]')
    INVESTMENT_LOCATOR=(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/h2[2]')
    CREDIT_LOCATOR=(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/h2[3]')
    LOAN_LOCATOR=(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/h2[4]')

    def click_signin(self):
        self.click_operation(self.SIGNIN_BTN_LOCATOR)

    def login(self):
        self.enter_text(self.LOGIN_FIELD, Config.USERNAME)
        self.enter_text(self.PASSWORD_FIELD, Config.PASSWORD)
        self.click_operation(self.SIGNIN_BTN)
        print('The user is successfully logged in.')

    def verify_account_summary(self):
        self.click_operation(self.ONLINE_LOCATOR)
        self.click_operation(self.ACCOUNT_LOCATOR)

    def verify_account_type(self):
        cash=self.find_web_element(self.CASH_LOCATOR).text
        assert "Cash Accounts" in cash
        print(f"{cash} visible successfully")
        investment=self.find_web_element(self.INVESTMENT_LOCATOR).text
        assert "Investment Accounts" in investment
        print(f'{investment} visible successfully')
        credit=self.find_web_element(self.CREDIT_LOCATOR).text
        assert "Credit Accounts" in credit
        print(f"{credit} visible successfully")
        loan=self.find_web_element(self.LOAN_LOCATOR).text
        assert "Loan Accounts" in loan
        print(f"{loan} visible successfully")
        
        