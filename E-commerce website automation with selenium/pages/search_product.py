from selenium.webdriver.common.by import By
from util.base_util import BasePage

class SearchProductsPage(BasePage):
    PRODUCT_BTN_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    SEARCH_BAR=(By.XPATH,"//*[@id='search_product']")
    SEARCH_BTN=(By.XPATH,"//*[@id='submit_search']")
    SEARCHED_PRODUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/h2")
    PRODUCT_NAME=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/p")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def click_products(self):
        self.wait_for_clickable(self.PRODUCT_BTN_LOCATOR)

    def enter_product(self,productname):
        self.enter_text(self.SEARCH_BAR,productname)
        self.wait_for_clickable(self.SEARCH_BTN)
    def searched_products(self):
        element1=self.wait_for_visibility(self.SEARCHED_PRODUCT).text
        assert element1=="SEARCHED PRODUCTS"
        print(f"{element1} showing")
    
    def product_search_matches(self):
        element=self.wait_for_visibility(self.PRODUCT_NAME).text
        assert element=="Blue Top"



