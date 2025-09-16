import pytest
from pages.add_review import AddReview   # adjust path to match your project

@pytest.mark.usefixtures("init_driver")
class TestCase21:

    def test_add_review(self):
        page = AddReview(self.driver)

        # Step 1: Verify homepage
        page.verify_homepage_visible()

        # Step 2: Go to Products page
        page.review_operations()

        # Step 3: Hover to all products (optional visual confirmation)
        page.move_to_all_products()

        # Step 4: Click on a product
        page.click_product()

        # Step 5: Move to review section
        page.move_to_review()

        # Step 6: Enter review details
        page.enter_details(
            name="Rakesh Goud",
            email="rakesh_review@test.com",
            text="This product quality is excellent! Highly recommended."
        )
