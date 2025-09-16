import pytest,time
from pages.verify_scrollup_without_arrow import ScrollUP

@pytest.mark.usefixtures("init_driver")
class TestCase26:
    def test_verify_scrollup(self):
        scroll_up=ScrollUP(self.driver)
        scroll_up.verify_homepage_visible()
        time.sleep(2)
        scroll_up.go_to_bottom()
        print("scrolled to bottom")
        time.sleep(2)
        scroll_up.go_to_top()
        print("scrolled to top")
        time.sleep(2)
        scroll_up.verify_text()
        time.sleep(2)