import pytest,time
from pages.verify_scrolling_using_arrow import ScrollOperation

@pytest.mark.usefixtures("init_driver")
class TestCase25:
    def test_verify_scrolling(self):
        scrolling=ScrollOperation(self.driver)
        scrolling.verify_homepage_visible()
        time.sleep(2)
        scrolling.go_to_bottom()
        time.sleep(2)
        scrolling.go_to_top()
        time.sleep(2)
        scrolling.msg_visible()
        time.sleep(2)