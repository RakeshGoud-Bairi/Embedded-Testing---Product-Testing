from selenium.webdriver.common.by import    By
from util.base_util import BasePage

class ScrollUP(BasePage):
    SUBSCRIPTION=(By.XPATH,"//*[@id='footer']/div[1]/div/div/div[2]/div/h2")
    TEXT=(By.XPATH,"//*[@id='slider-carousel']/div/div[1]/div[1]/h2")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def go_to_bottom(self):
        self.scroll_to_bottom()
        element=self.wait_for_visibility(self.SUBSCRIPTION).text
        assert element=="SUBSCRIPTION"
    
    def go_to_top(self):
        self.scroll_to_top()

    def verify_text(self):
        text_msg=self.wait_for_visibility(self.TEXT).text
        assert text_msg=="Full-Fledged practice website for Automation Engineers"
        print(f"{text_msg} visible successfully")
