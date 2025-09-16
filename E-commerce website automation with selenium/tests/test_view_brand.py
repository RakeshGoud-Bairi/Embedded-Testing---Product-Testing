import pytest
from pages.view_brand import ViewBrand

@pytest.mark.usefixtures("init_driver")
class TestCase19:
    def test_view_brand(self):
        brand=ViewBrand(self.driver)
        brand.verify_homepage_visible()
        brand.find_brand()
        brand.select_brand()