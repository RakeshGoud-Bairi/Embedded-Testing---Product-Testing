from selenium import webdriver

def get_browser(browser):
    if browser.lower()=="chrome":
        return webdriver.Chrome()
    elif browser.lower()=="edge":
        return webdriver.Edge()
    elif browser.lower()=="firefox":
        return webdriver.Firefox()
    else:
        raise ValueError(f"browser not found{browser}")