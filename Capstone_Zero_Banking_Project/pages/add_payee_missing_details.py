from base.base_page import BasePage
from config.config import Config
from selenium.webdriver.common.by import By

class AddPayeeMissingDetails(BasePage):
    SIGNIN_BTN_LOCATOR = (By.XPATH, '//*[@id="signin_button"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="user_login"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="user_password"]')
    SIGNIN_BTN = (By.XPATH, '//*[@id="login_form"]/div[2]/input')
    ONLINE_LOCATOR=(By.XPATH,'//*[@id="onlineBankingMenu"]/div/strong')
    ACCOUNT_LOCATOR=(By.XPATH,'//*[@id="account_summary_link"]')
    PAY_BILL=(By.XPATH,'//*[@id="pay_bills_tab"]/a')
    ADD_NEW_PAYEE=(By.XPATH,'//*[@id="tabs"]/ul/li[2]/a')
    NAME_LOCATOR=(By.XPATH,'//*[@id="np_new_payee_name"]')
    ADDRESS_LOCATOR=(By.XPATH,'//*[@id="np_new_payee_address"]')
    ACCOUNT_NAME=(By.XPATH,'//*[@id="np_new_payee_account"]')
    DETAILS_NEWPAYEE=(By.XPATH,'//*[@id="np_new_payee_details"]')
    SUBMIT_LOCATOR=(By.XPATH,'//*[@id="add_new_payee"]')
    SUCCESS_MSG=(By.XPATH,'//*[@id="alert_content"]')
    

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

    def add_new_payee(self,name,address,account,payee_details):
        self.click_operation(self.PAY_BILL)
        self.click_operation(self.ADD_NEW_PAYEE)
        self.enter_text(self.NAME_LOCATOR,name)
        self.enter_text(self.ADDRESS_LOCATOR,address)
        self.enter_text(self.ACCOUNT_NAME,account)
        self.enter_text(self.DETAILS_NEWPAYEE,payee_details)
        self.click_operation(self.SUBMIT_LOCATOR)
        
        self.driver.save_screenshot("screenshots/empty_details.png")
        print("screenshot saved beacuse, All fields are required.")