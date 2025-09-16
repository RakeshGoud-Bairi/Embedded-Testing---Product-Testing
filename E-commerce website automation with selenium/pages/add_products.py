from selenium.webdriver.common.by import By
from util.base_util import BasePage

class AddProducts(BasePage):
    PRODUCT_BTN_LOCATOR=(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a")
    MOVE_PRODUCT_1=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]")
    MOVE_PRODUCT_2=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]")
    ADD_FIRST_PRODUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a")
    CONTINUE_SHOPPING=(By.XPATH,"//*[@id='cartModal']/div/div/div[3]/button")
    ADD_SECOND_PRDOUCT=(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a")
    VIEW_CART=(By.XPATH,"//*[@id='cartModal']/div/div/div[2]/p[2]/a/u")
    VERIFY_PRODUCT_1=(By.XPATH,"//*[@id='product-1']/td[2]/h4/a")
    VERIFY_PRODUCT_2=(By.XPATH,"//*[@id='product-2']/td[2]/h4/a")
    PRICE_PRODUCT_1=(By.XPATH,"//*[@id='product-1']/td[3]/p")
    TOTAL_PRICE_1=(By.XPATH,"//*[@id='product-1']/td[5]/p")
    PRICE_PRODUCT_2=(By.XPATH,"//*[@id='product-2']/td[3]/p")
    TOTAL_PRICE_2=(By.XPATH,"//*[@id='product-2']/td[5]/p")
    QUANTITY_PRODUCT_1=(By.XPATH,"//*[@id='product-1']/td[4]/button")
    QUANTITY_PRODUCT_2=(By.XPATH,"//*[@id='product-2']/td[4]/button")



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

    def verify_products(self):
        element1=self.wait_for_visibility(self.VERIFY_PRODUCT_1).text
        assert element1=="Blue Top"
        print(f"PRODUCT-1:{element1}")
        element2=self.wait_for_visibility(self.VERIFY_PRODUCT_2).text
        assert element2=="Men Tshirt"
        print(f"PRODUCT-2:{element2}")
        print(f"Two products were verified {element1},{element2}")

    def product_prices(self):
        price1=self.wait_for_visibility(self.PRICE_PRODUCT_1).text
        assert price1=="Rs. 500"
        print(f"PRICE OF PRODUCT-1:{price1}")
        Total_price_1=self.wait_for_visibility(self.TOTAL_PRICE_1).text
        assert Total_price_1=="Rs. 500"
        print(f"TOTAL PRICE PRODUCT-1:{Total_price_1}")
        price2=self.wait_for_visibility(self.PRICE_PRODUCT_2).text
        assert price2=="Rs. 400"  
        print(f"PRICE OF PRODUCT-2:{price2}")
        Total_price_2=self.wait_for_visibility(self.TOTAL_PRICE_2).text
        assert Total_price_2=="Rs. 400"
        print(f"TOTAL PRICE PRODUCT-2:{Total_price_2}")

    def quantity(self):
        q1=self.wait_for_visibility(self.QUANTITY_PRODUCT_1).text
        assert q1=="1"
        print(f"Quantity:{q1}")
        q2=self.wait_for_visibility(self.QUANTITY_PRODUCT_2).text
        assert q2=="1"
        print(f"Quantity:{q2}")

