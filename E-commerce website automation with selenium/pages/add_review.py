from selenium.webdriver.common.by import By
import time
from util.base_util import BasePage

class AddReview(BasePage):
    PRODUCT_BTN_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    ALL_PRODUCTS_LOCATOR=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/h2")
    VIEW_PRODUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a")
    REVIEW=(By.XPATH,"/html/body/section/div/div/div[2]/div[3]/div[1]/ul/li/a")
    ENTER_NAME=(By.XPATH,"//*[@id='name']")
    ENTER_EMAIL=(By.XPATH,"//*[@id='email']")
    ENTER_REVIEW=(By.XPATH,"//*[@id='review']")
    SUBMIT=(By.XPATH,"//*[@id='button-review']")
    SUCCESS_MSG=(By.XPATH,"//*[@id='review-section']/div/div/span")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def review_operations(self):
        self.wait_for_clickable(self.PRODUCT_BTN_LOCATOR)

    def move_to_all_products(self):
        self.hover_element(self.ALL_PRODUCTS_LOCATOR)

    def click_product(self):
        self.wait_for_clickable(self.VIEW_PRODUCT)
    
    def move_to_review(self):
        self.hover_element(self.REVIEW)

    def enter_details(self,name,email,text):
        self.enter_text(self.ENTER_NAME,name)
        self.enter_text(self.ENTER_EMAIL,email)
        self.enter_text(self.ENTER_REVIEW,text)
        self.wait_for_clickable(self.SUBMIT)
        
        element=self.wait_for_visibility(self.SUCCESS_MSG).text
        assert element=="Thank you for your review."
        print(f"{element} visible successfully")