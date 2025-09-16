from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.common.action_chains import ActionChains  as AC
from selenium.webdriver import Keys
class BasePage:
    def __init__(self,driver,timeout=10):
        self.driver=driver
        self.timeout=timeout
        self.wait=WebDriverWait(self.driver,timeout=10)
        self.actions=AC(self.driver)

    def wait_for_visibility(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_clickable(self,locator):
        click=self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.click(click).perform()

    def wait_for_presence(self,locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def enter_text(self,locator,text):
        element=self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def select_dropdown_by_value(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_value(value)

    def select_dropdown_by_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        Select(element).select_by_visible_text(text)
    
    def scroll_to_element(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element
    
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

    def hover_element(self,locator):
        element=self.wait.until(EC.presence_of_element_located(locator))
        self.actions.move_to_element(element)

    def set_quantity(self,locator,value:int):
        element=self.driver.find_element(*locator)
        element.click()
        value=int(value)
        current_value=int(element.get_attribute("value"))

        while current_value < value:
            element.send_keys(Keys.ARROW_UP)
            current_value +=1
        while current_value > value:
            element.send_keys(Keys.ARROW_DOWN)
            current_value -=1
    