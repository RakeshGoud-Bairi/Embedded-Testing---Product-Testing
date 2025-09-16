from selenium.webdriver.common.by import By
import time
from util.base_util import BasePage

class RemoveProducts(BasePage):
    PRODUCT_BTN_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    MOVE_PRODUCT_1=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
    MOVE_PRODUCT_2=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]")
    ADD_FIRST_PRODUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a")
    CONTINUE_SHOPPING=(By.XPATH,"//*[@id='cartModal']/div/div/div[3]/button")
    ADD_SECOND_PRDOUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a")
    VIEW_CART=(By.XPATH,"//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    REMOVE_BTN=(By.XPATH,"//*[@id='product-1']/td[6]/a")
    REMOVE_BTN_2=(By.XPATH,"//*[@id='product-2']/td[6]/a")
    CART_MSG=(By.XPATH,"//*[@id='empty_cart']/p")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def click_products(self):
        self.wait_for_clickable(self.PRODUCT_BTN_LOCATOR)

    def move_to_element(self):
        self.hover_element(self.MOVE_PRODUCT_1)
    def add_product(self):
        self.wait_for_clickable(self.ADD_FIRST_PRODUCT)
        self.wait_for_clickable(self.CONTINUE_SHOPPING)
        self.hover_element(self.MOVE_PRODUCT_2)
        self.wait_for_clickable(self.ADD_SECOND_PRDOUCT)

    def click_cart(self):
        self.wait_for_clickable(self.VIEW_CART)

    def remove_product(self):
        self.wait_for_clickable(self.REMOVE_BTN)
        time.sleep(1)
        self.wait_for_clickable(self.REMOVE_BTN_2)

    def cart_msg(self):
        element=self.wait_for_visibility(self.CART_MSG).text
        assert element=="Cart is empty! Click here to buy products."
        print(f"{element} visible successfully")
