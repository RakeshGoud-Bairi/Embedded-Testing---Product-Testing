from selenium.webdriver.common.by import By
from util.base_util import BasePage

class SubscriptionPage(BasePage):
    EMAIL_LOCATOR=(By.XPATH,"//*[@id='susbscribe_email']")
    SUBMIT=(By.XPATH,"//*[@id='subscribe']")
    SUCCESS_MSG=(By.XPATH,"//div[contains(@class,'alert-success')]")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")
    
    def scroll(self):
        self.scroll_to_bottom()

    def enter_email(self,email):
        self.enter_text(self.EMAIL_LOCATOR,email)
        self.wait_for_clickable(self.SUBMIT)

    def alert(self):
        element=self.wait_for_visibility(self.SUCCESS_MSG).text
        print(f"alert msg:{element}")
        
        
        