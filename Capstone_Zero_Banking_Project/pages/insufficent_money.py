from base.base_page import BasePage
from config.config import Config
from selenium.webdriver.common.by import By

class InsufficentFundTransfer(BasePage):
    SIGNIN_BTN_LOCATOR = (By.XPATH, '//*[@id="signin_button"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="user_login"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="user_password"]')
    SIGNIN_BTN = (By.XPATH, '//*[@id="login_form"]/div[2]/input')
    ONLINE_LOCATOR=(By.XPATH,'//*[@id="onlineBankingMenu"]/div')
    ACCOUNT_LOCATOR=(By.XPATH,'//*[@id="account_summary_link"]')
    FUND_LOCATOR=(By.XPATH,'//*[@id="transfer_funds_tab"]/a')
    FROM_ACC=(By.ID,'tf_fromAccountId')
    TO_ACC=(By.ID,'tf_toAccountId')
    ENTER_MONEY=(By.XPATH,'//*[@id="tf_amount"]')
    DISCRIPTION=(By.XPATH,'//*[@id="tf_description"]')
    CONTINUE_BTN=(By.XPATH,'//*[@id="btn_submit"]')
    SUBMIT_BTN=(By.XPATH,'//*[@id="btn_submit"]')
    SUCCESS_MSG=(By.XPATH,'//*[@id="transfer_funds_content"]/div/div/div[1]')
    COMPLETE_TRANSACTION=(By.XPATH,"//*[@id='transfer_funds_content']/div/div/div[2]/div")

    

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
        self.click_operation(self.FUND_LOCATOR)

    def transfer_fund(self,value):
        self.click_operation(self.FUND_LOCATOR)
        self.select_dropdown_by_value(self.FROM_ACC,str(value))
    def select(self,value):
        self.select_dropdown_by_value(self.TO_ACC,str(value))
        
    def enter_money(self,money,msg):
        self.enter_text(self.ENTER_MONEY,money)
        self.enter_text(self.DISCRIPTION,msg)
        self.click_operation(self.CONTINUE_BTN)
        self.click_operation(self.SUBMIT_BTN)
        print("Insufficient Money in the account")