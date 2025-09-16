import pytest
from pages.add_recommended_product import AddRecommendedProduct

@pytest.mark.usefixtures("init_driver")
class TestCase22:
    def test_add_recommended_product(self):
        add=AddRecommendedProduct(self.driver)
        add.verify_homepage_visible()
        add.go_to_bottom()
        add.add_item()