from base.base_page import BasePage
from config.config import Config
from selenium.webdriver.common.by import By

class PayBillWithOutAmount(BasePage):
    SIGNIN_BTN_LOCATOR = (By.XPATH, '//*[@id="signin_button"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="user_login"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="user_password"]')
    SIGNIN_BTN = (By.XPATH, '//*[@id="login_form"]/div[2]/input')
    ONLINE_LOCATOR=(By.XPATH,'//*[@id="onlineBankingMenu"]/div/strong')
    ACCOUNT_LOCATOR=(By.XPATH,'//*[@id="account_summary_link"]')
    PAY_BILL=(By.XPATH,'//*[@id="pay_bills_tab"]/a')
    AMOUNT=(By.XPATH,'//*[@id="sp_amount"]')
    DATE=(By.XPATH,'//*[@id="sp_date"]')
    MSG_LOCATOR=(By.XPATH,'//*[@id="sp_description"]')
    PAY_BTN=(By.XPATH,'//*[@id="pay_saved_payees"]')
    

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
        
    def pay_bill(self,amount,date,msg):
        self.click_operation(self.PAY_BILL)
        self.enter_text(self.AMOUNT,amount)
        self.enter_date(self.DATE,date)
        self.enter_text(self.MSG_LOCATOR,msg)
        self.click_operation(self.PAY_BTN)
        
        self.driver.save_screenshot("screenshots/empty_amount.png")
        print("screenshot saved beacuse, Amount field cannot be empty.")
        


