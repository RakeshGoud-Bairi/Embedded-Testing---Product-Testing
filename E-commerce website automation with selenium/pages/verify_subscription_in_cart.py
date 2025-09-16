from selenium.webdriver.common.by import By
from util.base_util import BasePage

class CartSubscriptionPage(BasePage):
    CART_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a")
    SUBSCRIPTION_LOCATOR=(By.XPATH,"//*[@id='footer']/div[1]/div/div/div[2]/div/h2")
    EMAIL_LOCATOR=(By.XPATH,"//*[@id='susbscribe_email']")
    SUBMIT=(By.XPATH,"//*[@id='subscribe']")
    SUCCESS_MSG=(By.XPATH,"//div[contains(@class,'alert-success')]")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def click(self):
        self.wait_for_clickable(self.CART_LOCATOR)
    
    def scroll(self):
        element=self.wait_for_visibility(self.SUBSCRIPTION_LOCATOR).text
        assert element=="SUBSCRIPTION"
        print(f"{element}")

    def enter_email(self,email):
        self.enter_text(self.EMAIL_LOCATOR,email)
        self.wait_for_clickable(self.SUBMIT)

    def alert(self):
        element=self.wait_for_visibility(self.SUCCESS_MSG).text
        print(f"alert msg:{element}")

