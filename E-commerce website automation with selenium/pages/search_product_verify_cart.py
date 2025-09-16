from time import sleep
from selenium.webdriver.common.by import By
from util.base_util import BasePage

class SearchProductVerify(BasePage):
    PRODUCT_BTN_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    SEARCH_BAR=(By.XPATH,"//*[@id='search_product']")
    SEARCH_BTN=(By.XPATH,"//*[@id='submit_search']")
    SEARCHED_PRODUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/h2")
    ADD_PRODUCT_1=(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[1]/div[1]/a")
    ADD_PRODUCT_2=(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/div[3]/div/div[1]/div[1]/a")
    ADD_PRODUCT_3=(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/div[4]/div/div[1]/div[1]/a")
    ADD_PRODUCT_4=(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/div[5]/div[1]/div[1]/div[1]/a")
    ADD_PRODUCT_5=(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/div[6]/div/div[1]/div[1]/a")
    ADD_PRODUCT_6=(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/div[7]/div/div[1]/div[1]/a")
    CONTINUE_SHOPPING=(By.XPATH,"//*[@id='cartModal']/div/div/div[3]/button")
    VIEW_CART=(By.XPATH,"//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    SIGNUP_BTN=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
    EMAIL_LOCATOR=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/input[2]")
    PASSWORD=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/input[3]")
    LOGIN_BTN=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/button")
    CART_BTN=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a")
    REMOVE_PRODUCT_1=(By.XPATH,"//*[@id='product-2']/td[6]/a")
    REMOVE_PRODUCT_2=(By.XPATH,"//*[@id='product-29']/td[6]/a")
    REMOVE_PRODUCT_3=(By.XPATH,"//*[@id='product-30']/td[6]/a")
    REMOVE_PRODUCT_4=(By.XPATH,"//*[@id='product-31']/td[6]/a")
    REMOVE_PRODUCT_5=(By.XPATH,"//*[@id='product-43']/td[6]/a")
    REMOVE_PRODUCT_6=(By.XPATH,"//*[@id='product-28']/td[6]/a")
    EMPTY_CART=(By.XPATH,"//*[@id='empty_cart']/p")

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

    def add_products_to_cart(self):
        self.wait_for_clickable(self.ADD_PRODUCT_1)
        self.wait_for_clickable(self.CONTINUE_SHOPPING)
        self.wait_for_clickable(self.ADD_PRODUCT_2)
        self.wait_for_clickable(self.CONTINUE_SHOPPING)
        self.wait_for_clickable(self.ADD_PRODUCT_3)
        self.wait_for_clickable(self.CONTINUE_SHOPPING)
        self.wait_for_clickable(self.ADD_PRODUCT_4)
        self.wait_for_clickable(self.CONTINUE_SHOPPING)
        self.wait_for_clickable(self.ADD_PRODUCT_5)
        self.wait_for_clickable(self.CONTINUE_SHOPPING)
        self.wait_for_clickable(self.ADD_PRODUCT_6)
        self.wait_for_clickable(self.VIEW_CART)
    def click_signup(self):
        self.wait_for_clickable(self.SIGNUP_BTN)
    def fill_details(self,email,password):
        self.enter_text(self.EMAIL_LOCATOR,email)
        self.enter_text(self.PASSWORD,password)
        self.wait_for_clickable(self.LOGIN_BTN)

    def click_cart(self):
        self.wait_for_clickable(self.CART_BTN)

    def remove_products(self):
        self.wait_for_clickable(self.REMOVE_PRODUCT_1)
        sleep(1)
        self.wait_for_clickable(self.REMOVE_PRODUCT_2)
        sleep(1)
        self.wait_for_clickable(self.REMOVE_PRODUCT_3)
        sleep(1)
        self.wait_for_clickable(self.REMOVE_PRODUCT_4)
        sleep(1)
        self.wait_for_clickable(self.REMOVE_PRODUCT_5)
        sleep(1)
        self.wait_for_clickable(self.REMOVE_PRODUCT_6)
        sleep(1)
    def empty_cart(self):
        element=self.wait_for_visibility(self.EMPTY_CART).text
        assert element=="Cart is empty! Click here to buy products."
        print(f"{element} visible successfully")
        

