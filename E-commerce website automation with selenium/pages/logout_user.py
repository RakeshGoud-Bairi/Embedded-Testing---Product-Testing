from selenium.webdriver.common.by import   By
from util.base_util import  BasePage

class LogoutUser(BasePage):
    SIGIN_BTN=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
    EMAIL_LOCATOR=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/input[2]")
    PASSWORD=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/input[3]")
    LOGIN_BTN=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/button")
    TITLE_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")
    LOGOUT_LOCATOR=(By.XPATH,"//a[text()=' Logout']")
    BACK_LOGIN_PAGE=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/h2")


    def login(self,email,password):
        self.wait_for_clickable(self.SIGIN_BTN)
        self.enter_text(self.EMAIL_LOCATOR,email)
        self.enter_text(self.PASSWORD,password)
        self.wait_for_clickable(self.LOGIN_BTN)

    def check_title_matches(self):
        element=self.wait_for_visibility(self.TITLE_LOCATOR).text
        assert "Logged in as Rakesh"==element
        print(f"{element}")
    def logout(self):
        self.wait_for_clickable(self.LOGOUT_LOCATOR)

    def navigate_login_page(self):
        element=self.wait_for_visibility(self.BACK_LOGIN_PAGE).text
        assert "Login to your account"==element
        print(f"navigated to login page:{element}")
