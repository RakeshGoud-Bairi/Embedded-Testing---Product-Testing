from selenium.webdriver.common.by import By
from util.base_util import BasePage

class ViewCategory(BasePage):
    CATEGORY_LOCATOR=(By.XPATH,"/html/body/section[2]/div/div/div[1]/div/h2")
    ENTER_CATEGORY=(By.XPATH,"//*[@id='accordian']/div[1]/div[1]/h4/a/span/i")
    DRESS_LOCATOR=(By.XPATH,"//*[@id='Women']/div/ul/li[1]/a")
    DRESS_TITLE=(By.XPATH,"/html/body/section/div/div[2]/div[2]/div/h2")
    MEN_CATEGORY=(By.XPATH,"//*[@id='accordian']/div[2]/div[1]/h4/a/span")
    MEN_SUB_CATEGORY=(By.XPATH,"//*[@id='Men']/div/ul/li[1]/a")
    MEN_TITLE=(By.XPATH,"/html/body/section/div/div[2]/div[2]/div/h2")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def find_category(self):
        self.hover_element(self.CATEGORY_LOCATOR)
        print("moved to category block")
        self.wait_for_clickable(self.ENTER_CATEGORY)
        print("clicked the women category")
        self.wait_for_clickable(self.DRESS_LOCATOR)
        print("clicked the dress in women category")
        element=self.wait_for_visibility(self.DRESS_TITLE).text
        '''assert element=="WOMEN -  DRESS PRODUCTS"'''
        print(f"{element} visible successfully")
        self.wait_for_clickable(self.MEN_CATEGORY)
        print("selected men category")
        self.wait_for_clickable(self.MEN_SUB_CATEGORY)
        print("clicked men sub category")
        element2=self.wait_for_visibility(self.MEN_TITLE).text
        '''assert element2=="MEN -  TSHIRTS PRODUCTS"'''
        print(f"{element2} visible successfully")
        print(f"successfully navigated from {element} to {element2}")