import pytest
from config.config import ConfigPage
from util.browser_factory import get_driver

@pytest.fixture(scope="class")
def init_driver(request):
    driver=get_driver('chrome')
    driver.maximize_window()
    driver.get(ConfigPage.BASE_URL)
    request.cls.driver=driver
    yield
    print("All test cases passed")
    driver.quit()

