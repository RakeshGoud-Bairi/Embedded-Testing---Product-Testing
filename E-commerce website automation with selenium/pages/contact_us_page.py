from selenium.webdriver.common.by import By
from util.base_util import BasePage
import os

class ContactUs(BasePage):
    CONTACT_US=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[8]/a")
    POP_UP_MSG=(By.XPATH,"//*[@id='contact-page']/div[2]/div[1]/div/h2")
    ENTER_NAME=(By.XPATH,"//*[@id='contact-us-form']/div[1]/input")
    ENTER_EMAIL=(By.XPATH,"//*[@id='contact-us-form']/div[2]/input")
    SUBJECT_MSG=(By.XPATH,"//*[@id='contact-us-form']/div[3]/input")
    MESSAGE=(By.XPATH,"//*[@id='message']")
    ADD_FILE=(By.XPATH,"//*[@id='contact-us-form']/div[5]/input")
    SUBMIT=(By.XPATH,"//*[@id='contact-us-form']/div[6]/input")
    SUCCESS_MSG=(By.XPATH,"//*[@id='contact-page']/div[2]/div[1]/div/div[2]")
    HOME_PAGE=(By.XPATH,"//*[@id='form-section']/a/span")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def click_on_contactus(self):
        self.wait_for_clickable(self.CONTACT_US)

    def fill_details(self,name,email,subject,message):
        element=self.wait_for_visibility(self.POP_UP_MSG).text
        assert "GET IN TOUCH"==element
        print(f"{element} visible successfully")
        self.enter_text(self.ENTER_NAME,name)
        self.enter_text(self.ENTER_EMAIL,email)
        self.enter_text(self.SUBJECT_MSG,subject)
        self.enter_text(self.MESSAGE,message)

    def add_path(self):
        filepath=os.path.abspath(r"C:\Users\DELL\Downloads\RAM00690.jpg")
        self.enter_text(self.ADD_FILE,filepath)
        print("file uploaded successfully")
        self.wait_for_clickable(self.SUBMIT)

    def conform_alert(self):
        alert=self.driver.switch_to.alert
        alert.accept()
        
    def success_msg(self):
        element=self.wait_for_visibility(self.SUCCESS_MSG).text
        print(f"{element} visible successfully")
    
    def return_home(self):
        self.wait_for_clickable(self.HOME_PAGE)
