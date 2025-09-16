from selenium.webdriver.common.by import By
from util.Base_utils import BasePage
from selenium.webdriver.common.action_chains import ActionChains as AC


class BookAppoinment:
    MAKE_APPOINMENT_BTN=(By.XPATH,"//*[@id='btn-make-appointment']")
    USERNAME=(By.XPATH,"//*[@id='txt-username']")
    PASSWORD=(By.XPATH,"//*[@id='txt-password']")
    SUBMIT=(By.XPATH,"//*[@id='btn-login']")
    CHOOSE_FACILITY=(By.XPATH,"//*[@id='combo_facility']/option[3]")
    APPLY_FOR_ADDMISSION=(By.XPATH,"//*[@id='appointment']/div/div/form/div[2]/div/label")
    HEALTH_PROGRAM=(By.XPATH,"//*[@id='appointment']/div/div/form/div[3]/div/label[1]")
    DATE_PICKER=(By.XPATH,"//*[@id='txt_visit_date']")
    SHOW_DATE=(By.XPATH,"/html/body/div/div[1]/table/thead/tr[2]/th[2]")
    CLICK_NEXT=(By.XPATH,"/html/body/div/div[1]/table/thead/tr[2]/th[3]")
    SELECT_DATE=(By.XPATH,"/html/body/div/div[1]/table/tbody/tr[5]/td[3]")
    COMMENTS=(By.XPATH,"//*[@id='txt_comment']")
    BOOK_APPOINMENT=(By.XPATH,"//*[@id='btn-book-appointment']")
    BACK_HOME=(By.XPATH,"//a[text()='Go to Homepage']")

    def __init__(self,driver):
        self.driver=driver
        self.actions=AC(driver)
        self.base=BasePage(driver)
        

    def book_appoinment(self):
        click=self.base.wait_for_presence(self.MAKE_APPOINMENT_BTN)
        self.actions.click(click).perform()

    def login(self,username,password):
        self.base.wait_for_visibility_send_keys(self.USERNAME,username)
        self.base.wait_for_visibility_send_keys(self.PASSWORD,password)
        self.base.wait_for_clickable(self.SUBMIT)

    def start_process(self):
        self.driver.find_element(*self.CHOOSE_FACILITY)
        self.base.wait_for_clickable(self.APPLY_FOR_ADDMISSION)
        self.base.wait_for_clickable(self.HEALTH_PROGRAM)
        

    def choose_date(self):
        self.base.wait_for_clickable(self.DATE_PICKER)
        obj1=self.base.wait_for_visibility(self.SHOW_DATE).text
        month_year="August 2025"
        while True:
            if obj1==month_year:
                break
            self.base.wait_for_clickable(self.CLICK_NEXT)
        self.base.wait_for_clickable(self.SELECT_DATE)
    
    def add_comment(self,text):
        self.base.wait_for_visibility_send_keys(self.COMMENTS,text)

    def submit(self):
        self.base.wait_for_clickable(self.BOOK_APPOINMENT)
    def back_home(self):
        self.base.wait_for_clickable(self.BACK_HOME)

    def take_screen_shot(self) :
        self.driver.save_screenshot("entire_page.png")
