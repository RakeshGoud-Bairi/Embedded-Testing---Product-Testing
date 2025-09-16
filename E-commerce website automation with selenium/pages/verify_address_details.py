from selenium.webdriver.common.by import By
from util.base_util import BasePage

class VerifyAddress(BasePage):
    SIGIN_BTN=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
    NAME_LOCATOR=(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/input[2]")
    EMAIL_LOCATOR=(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/input[3]")
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
    TITLE_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")
    PRODUCT_BTN_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    MOVE_PRODUCT_1=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
    MOVE_PRODUCT_2=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]")
    ADD_FIRST_PRODUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a")
    CONTINUE_SHOPPING=(By.XPATH,"//*[@id='cartModal']/div/div/div[3]/button")
    ADD_SECOND_PRDOUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a")
    CHECKOUT_BTN=(By.XPATH,"//*[@id='do_action']/div[1]/div/div/a")
    VIEW_CART=(By.XPATH,"//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    DELETE_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")
    DELETE_CONTINUE=(By.XPATH,"//*[@id='form']/div/div/div/div/a")
    DELIVERY_ADDRESS=(By.XPATH,"//*[@id='address_delivery']")
    BILLING_ADDRESS=(By.XPATH,"//*[@id='address_invoice']")



    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def new_user_signup(self,Name,Email):
        self.wait_for_clickable(self.SIGIN_BTN)
        self.enter_text(self.NAME_LOCATOR,Name)
        self.enter_text(self.EMAIL_LOCATOR,Email)
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

    def click_product(self):
        self.wait_for_clickable(self.PRODUCT_BTN_LOCATOR)
        self.hover_element(self.MOVE_PRODUCT_1)
        self.wait_for_clickable(self.ADD_FIRST_PRODUCT)
        self.wait_for_clickable(self.CONTINUE_SHOPPING)
        self.hover_element(self.MOVE_PRODUCT_2)
        self.wait_for_clickable(self.ADD_SECOND_PRDOUCT)
        self.wait_for_clickable(self.VIEW_CART)

    def proceed_to_bill(self):
        self.wait_for_clickable(self.CHECKOUT_BTN)
    
    def verify_address(self):
        element=self.wait_for_visibility(self.DELIVERY_ADDRESS).text
        element1=self.wait_for_visibility(self.BILLING_ADDRESS).text
        print(f"{element} visible data")
        print(f"{element1} visible data")
        assert self.firstname in element
        assert self.lastname in element
        assert self.address in element
        assert self.city in     element
        assert self.zipcode in element
        assert self.mobile in   element
        print("Delivery and Billing addresses match registration details")

    def delete_account(self):
        self.wait_for_clickable(self.DELETE_LOCATOR)
        self.wait_for_clickable(self.DELETE_CONTINUE)