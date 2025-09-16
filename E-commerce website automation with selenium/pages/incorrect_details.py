from selenium.webdriver.common.by import By
from util.base_util import BasePage

class InCorrectDetails(BasePage):
    SIGIN_BTN=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
    EMAIL_LOCATOR=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/input[2]")
    PASSWORD=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/input[3]")
    LOGIN_BTN=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/button")
    ERROR_MSG=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/p")

    def login(self,email,password):
        self.wait_for_clickable(self.SIGIN_BTN)
        self.enter_text(self.EMAIL_LOCATOR,email)
        self.enter_text(self.PASSWORD,password)
        self.wait_for_clickable(self.LOGIN_BTN)
    
    def error_msg(self):
        msg=self.wait_for_visibility(self.ERROR_MSG).text
        assert "Your email or password is incorrect!"==msg
        print(f"error msg: {msg}")