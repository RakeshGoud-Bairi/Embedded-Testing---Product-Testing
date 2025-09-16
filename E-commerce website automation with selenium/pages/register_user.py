from selenium.webdriver.common.by import By
from util.base_util import BasePage

class RegisterPage(BasePage):
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
    DELETE_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")
    DELETE_CONTINUE=(By.XPATH,"//*[@id='form']/div/div/div/div/a")
    TITLE_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[10]/a")

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
        
    def delete_account(self):
        self.wait_for_clickable(self.DELETE_LOCATOR)
        self.wait_for_clickable(self.DELETE_CONTINUE)
