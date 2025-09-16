from selenium.webdriver.common.by import By
from util.base_util import BasePage

class Add4Products(BasePage):
    PRODUCT_BTN_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    MOVE_PRODUCT_1=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
    VIEW_PRODUCT=(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/ul/li/a")
    QUANTITY_BTN=(By.ID,"quantity")
    ADD_CART=(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button")
    VIEW_CART=(By.XPATH,"//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    PRODUCT_DETAILS=(By.XPATH,"//*[@id='product-1']/td[2]/h4/a")
    PRICE=(By.XPATH,"//*[@id='product-1']/td[3]/p")
    QUANTITY=(By.XPATH,"//*[@id='product-1']/td[4]/button")


    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def click_products(self):
        self.wait_for_clickable(self.PRODUCT_BTN_LOCATOR)

    def move_to_element(self):
        self.hover_element(self.MOVE_PRODUCT_1)

    def view_details(self):
        self.wait_for_clickable(self.VIEW_PRODUCT)

    def quantity(self,value):
        self.set_quantity(self.QUANTITY_BTN,value)
        
    
    def add_to_cart(self):
        self.wait_for_clickable(self.ADD_CART)
        self.wait_for_clickable(self.VIEW_CART)

    def product_details(self):
        element1=self.wait_for_visibility(self.PRODUCT_DETAILS).text
        assert element1=="Blue Top"
        print(f"Product Name:{element1}")
        price=self.wait_for_visibility(self.PRICE).text
        assert price=="Rs. 500"
        print(f"Price:{price}")
        quantity=self.wait_for_visibility(self.QUANTITY).text
        assert quantity=="4"
        print(f"Quantity:{quantity}")