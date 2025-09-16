import pytest
from pages.view_category import ViewCategory

@pytest.mark.usefixtures("init_driver")
class TestCase18:
    def test_view_category(self):
        view=ViewCategory(self.driver)
        view.verify_homepage_visible()
        view.find_category()