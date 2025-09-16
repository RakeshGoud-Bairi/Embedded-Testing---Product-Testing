from selenium.webdriver.common.by import    By
from util.base_util import BasePage

class ViewBrand(BasePage):
    BRAND_LOCATOR=(By.XPATH,"/html/body/section[2]/div/div/div[1]/div/div[2]/h2")
    POLO_BRAND=(By.XPATH,"/html/body/section[2]/div/div/div[1]/div/div[2]/div/ul/li[1]/a")
    POLO_BRAND_PRODUCTS=(By.XPATH,"/html/body/section/div/div[2]/div[2]/div/h2")
    MADAME_LOCATOR=(By.XPATH,"/html/body/section/div/div[2]/div[1]/div[1]/div[2]/div/ul/li[3]/a")
    MADAME_BRAND_PRODUCTS=(By.XPATH,"/html/body/section/div/div[2]/div[2]/div/h2")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def find_brand(self):
        self.hover_element(self.BRAND_LOCATOR)
        element=self.wait_for_visibility(self.BRAND_LOCATOR).text
        print(f"{element} navigated to brand")

    def select_brand(self):
        self.wait_for_clickable(self.POLO_BRAND)
        title=self.wait_for_visibility(self.POLO_BRAND_PRODUCTS).text
        assert title=="BRAND - POLO PRODUCTS"
        print(f"{title} are visible successfully")
        print("navigate to another brand")
        self.wait_for_clickable(self.MADAME_LOCATOR)
        titile2=self.wait_for_visibility(self.MADAME_BRAND_PRODUCTS).text
        assert titile2=="BRAND - MADAME PRODUCTS"
        print(f"{titile2} are visible successfully")
        print("process done successfully")
