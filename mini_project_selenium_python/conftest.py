import pytest
from util.browser_factory import get_browser

@pytest.fixture(scope="class")
def init_driver(request):
    driver=get_browser('edge')
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.quit()
    