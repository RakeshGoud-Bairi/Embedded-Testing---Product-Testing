from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self,driver,timeout=20):
        self.driver=driver
        self.timeout=timeout
        self.wait=WebDriverWait(driver,timeout=20)

    def load_browser(self):
        self.driver.get(self.url)

    def wait_for_visibility(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(EC.visibility_of_element_located(locator))
    
    def wait_for_clickable(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(EC.element_to_be_clickable(locator)).click()
    
    def wait_for_presence(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(EC.presence_of_element_located(locator))
    
    def wait_for_visibility_send_keys(self,locator,text):
        return WebDriverWait(self.driver,self.timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)
        
    