from selenium.webdriver.common.by import   By
from util.base_util import  BasePage

class LoginAndCheckout(BasePage):
    SIGIN_BTN=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
    EMAIL_LOCATOR=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/input[2]")
    PASSWORD=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/input[3]")
    LOGIN_BTN=(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/button")
    TITLE_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")
    PRODUCT_BTN_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    MOVE_PRODUCT_1=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
    MOVE_PRODUCT_2=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]")
    ADD_FIRST_PRODUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a")
    CONTINUE_SHOPPING=(By.XPATH,"//*[@id='cartModal']/div/div/div[3]/button")
    ADD_SECOND_PRDOUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a")
    VIEW_CART=(By.XPATH,"//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    CHECKOUT_BTN=(By.XPATH,"//*[@id='do_action']/div[1]/div/div/a")
    TEXT_MSG=(By.XPATH,"//*[@id='ordermsg']/textarea")
    PLACE_ORDER_BTN=(By.XPATH,"//*[@id='cart_items']/div/div[7]/a")
    NAME_ON_CARD=(By.XPATH,"//*[@id='payment-form']/div[1]/div/input")
    CARD_NO=(By.XPATH,"//*[@id='payment-form']/div[2]/div/input")
    CVC_NO=(By.XPATH,"//*[@id='payment-form']/div[3]/div[1]/input")
    MONTH=(By.XPATH,"//*[@id='payment-form']/div[3]/div[2]/input")
    YEAR=(By.XPATH,"//*[@id='payment-form']/div[3]/div[3]/input")
    PAY_ORDER_BTN=(By.XPATH,"//*[@id='submit']")
    SUCCESS_MSG=(By.XPATH,"//*[@id='form']/div/div/div/p")
    AFTER_CONTINUE=(By.XPATH,"//*[@id='form']/div/div/div/div/a")
    DELETE_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")
    DELETE_CONTINUE=(By.XPATH,"//*[@id='form']/div/div/div/div/a")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def login(self,email,password):
        self.wait_for_clickable(self.SIGIN_BTN)
        self.enter_text(self.EMAIL_LOCATOR,email)
        self.enter_text(self.PASSWORD,password)
        self.wait_for_clickable(self.LOGIN_BTN)
    
    def check_title_matches(self):
        element=self.wait_for_visibility(self.TITLE_LOCATOR).text
        assert "Logged in as Rakesh"==element
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
    
    def proceed_to_checkout(self):
        self.wait_for_clickable(self.CHECKOUT_BTN)

    def send_msg(self,text):
        self.enter_text(self.TEXT_MSG,text)
        self.wait_for_clickable(self.PLACE_ORDER_BTN)

    def card_details(self,name,number,cvc,month,year):
        self.enter_text(self.NAME_ON_CARD,name)
        self.enter_text(self.CARD_NO,number)
        self.enter_text(self.CVC_NO,cvc)
        self.enter_text(self.MONTH,month)
        self.enter_text(self.YEAR,year)
        self.wait_for_clickable(self.PAY_ORDER_BTN)

    def order_success(self):
        element=self.wait_for_visibility(self.SUCCESS_MSG).text
        assert element=="Congratulations! Your order has been confirmed!"
        print(f"{element} visible successfully")
        self.wait_for_clickable(self.AFTER_CONTINUE)

    