from selenium.webdriver.common.by import By
from util.base_util import BasePage

class CheckOut(BasePage):
    PRODUCT_BTN_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    MOVE_PRODUCT_1=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
    MOVE_PRODUCT_2=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]")
    ADD_FIRST_PRODUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a")
    CONTINUE_SHOPPING=(By.XPATH,"//*[@id='cartModal']/div/div/div[3]/button")
    ADD_SECOND_PRDOUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a")
    VIEW_CART=(By.XPATH,"//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    CHECKOUT_BTN=(By.XPATH,"//*[@id='do_action']/div[1]/div/div/a")
    REGISTER_BTN=(By.XPATH,"//*[@id='checkoutModal']/div/div/div[2]/p[2]/a/u")
    ENTER_NAME=(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/input[2]")
    ENTER_EMAIL=(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/input[3]")
    SIGNUP_BTN=(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/button")
    SELECT_BTN=(By.XPATH,"//*[@id='id_gender1']")
    PASSWORD_LOCATOR=(By.ID,"password")
    DATE_LOCATOR=(By.ID,"days")
    MONTH_LOCATOR=(By.ID,"months")
    YEAR_LOCATOR=(By.ID,"years")
    NEWSLETTER_LOCATOR=(By.XPATH,"//*[@id='newsletter']")
    FIRST_NAME=(By.ID,"first_name")
    LAST_NAME=(By.ID,"last_name")
    COMPANY=(By.ID,"company")
    ADDRESS=(By.ID,"address1")
    STATE_LOCATOR=(By.ID,"state")
    CITY_LOCATOR=(By.ID,"city")
    ZIPCODE_LOCATOR=(By.ID,"zipcode")
    MOBILE_NUMBER=(By.ID,"mobile_number")
    CREATE_ACCOUNT=(By.XPATH,"//*[@id='form']/div/div/div/div[1]/form/button")
    CONTINUE_LOCATOR=(By.XPATH,"//*[@id='form']/div/div/div/div/a")
    DELETE_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")
    DELETE_CONTINUE=(By.XPATH,"//*[@id='form']/div/div/div/div/a")
    TITLE_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")
    CART_BTN=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[3]/a")
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
    
    def proceed_to_checkout(self):
        self.wait_for_clickable(self.CHECKOUT_BTN)

    def register(self):
        self.wait_for_clickable(self.REGISTER_BTN)

    def new_user_signup(self,Name,Email):
        self.enter_text(self.ENTER_NAME,Name)
        self.enter_text(self.ENTER_EMAIL,Email)
        self.wait_for_clickable(self.SIGNUP_BTN)

    def enter_information(self):
        self.wait_for_clickable(self.SELECT_BTN)

    def enter_password(self,password):
        self.enter_text(self.PASSWORD_LOCATOR,password)

    def date(self,value=6):
        self.select_dropdown_by_value(self.DATE_LOCATOR,str(value))
       

    def month(self,text="August"):
        self.select_dropdown_by_text(self.MONTH_LOCATOR,str(text))

    def year(self,value=2002)  :
        self.select_dropdown_by_value(self.YEAR_LOCATOR,str(value))

    def new_sletter(self):
        self.wait_for_clickable(self.NEWSLETTER_LOCATOR)
    def enter_account_details(self,firstname,lastname,company,address,state,city,zipcode,mobile):
        self.enter_text(self.FIRST_NAME,firstname)
        self.enter_text(self.LAST_NAME,lastname)
        self.enter_text(self.COMPANY,company)
        self.enter_text(self.ADDRESS,address)
        self.enter_text(self.STATE_LOCATOR,state)
        self.enter_text(self.CITY_LOCATOR,city)
        self.enter_text(self.ZIPCODE_LOCATOR,zipcode)
        self.enter_text(self.MOBILE_NUMBER,mobile)

    def create_account(self):
        self.wait_for_clickable(self.CREATE_ACCOUNT)
        self.wait_for_clickable(self.CONTINUE_LOCATOR)

    def check_title_matches(self):
        element=self.wait_for_visibility(self.TITLE_LOCATOR).text
        assert "Logged in as Rakesh"==element

    def go_to_cart(self):
        self.wait_for_clickable(self.CART_BTN)
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

    def locate_delete(self):
        self.wait_for_clickable(self.DELETE_LOCATOR)
        self.wait_for_clickable(self.DELETE_CONTINUE)