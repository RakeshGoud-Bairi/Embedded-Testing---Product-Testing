from selenium.webdriver.common.by import By
from util.base_util import BasePage

class AddRecommendedProduct(BasePage):
    RECOMMENDED=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div[2]/h2")
    ADD_PRODUCT_TO_CART=(By.XPATH,"//*[@id='recommended-item-carousel']/div/div[1]/div[2]/div/div/div/a")
    VIEW_CART=(By.XPATH,"//*[@id='cartModal']/div/div/div[2]/p[2]/a")

    def verify_homepage_visible(self):
        assert "Automation Exercise" == self.driver.title
        print(f"title verified {self.driver.title}")

    def go_to_bottom(self):
        self.scroll_to_bottom()
        self.hover_element(self.RECOMMENDED)

    def add_item(self):
        self.wait_for_clickable(self.ADD_PRODUCT_TO_CART)
        self.wait_for_clickable(self.VIEW_CART)
        print("product is added to cart successfully")