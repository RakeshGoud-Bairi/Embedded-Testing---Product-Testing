from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.actions = ActionChains(self.driver)
    
    def find_web_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def finf_multiple_web_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.click(element).send_keys(text).perform()
    
    def remove_enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.click(element).key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND).send_keys(Keys.DELETE).send_keys(text).perform()
    
    def click_operation(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.click(element).perform()
    
    def context_click_opeartion(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.context_click(element).perform()
    
    def double_click_operation(self, locator):
        button = self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.double_click(button).perform()
    
    def presence_of_element(self, locator):
        button = self.wait.until(EC.presence_of_element_located(locator))
        self.actions.click(button).perform()

    def mouse_hover(self, locator):
        element = self.find_web_element(locator)
        self.actions.move_to_element(element).perform()

    def select_dropdown_by_value(self, locator, value):
        dropdown=self.driver.find_element(*locator)
        select=Select(dropdown)
        select.select_by_value(value)
    
    def enter_date(self,locator,date):
        date_str=self.driver.find_element(*locator)
        date_str.clear()
        date_str.send_keys(date)