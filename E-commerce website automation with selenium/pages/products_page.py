from selenium.webdriver.common.by import By
from util.base_util import BasePage

class ProductsPage(BasePage):
    PRODUCT_BTN_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    ALL_PRODUCTS_LOCATOR=(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/h2")
    VIEW_PRODUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a")
    PRODUCT_NAME=(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2")
    PRICE=(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span")
    AVAILABILTY=(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[2]")
    CONDITION=(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[3]")
    BRAND=(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[4]")
    CATEGORY=(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[1]")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def click_products(self):
        self.wait_for_clickable(self.PRODUCT_BTN_LOCATOR)

    def check_all_products(self):
        element=self.wait_for_visibility(self.ALL_PRODUCTS_LOCATOR)
        text=element.text

        print(f"{text} visible successfully")
        assert text=="ALL PRODUCTS"

    def click_view_product(self):
        self.wait_for_clickable(self.VIEW_PRODUCT)

    def verify_details(self):
        element=self.wait_for_visibility(self.PRODUCT_NAME).text
        print(f"PRODUCT NAME:{element}")
        assert element=="Blue Top"
        element1=self.wait_for_visibility(self.CATEGORY).text
        assert element1=="Category: Women > Tops"
        print(f"{element1}")
        price=self.wait_for_visibility(self.PRICE).text
        assert price=="Rs. 500"
        print(f"{price}")
        element2=self.wait_for_visibility(self.AVAILABILTY).text
        assert element2=="Availability: In Stock"
        print(f"{element2}")
        element3=self.wait_for_visibility(self.CONDITION).text
        assert element3=="Condition: New"
        print(f"{element3}")
        element4=self.wait_for_visibility(self.BRAND).text
        assert element4=="Brand: Polo"
        print(f"{element4}")