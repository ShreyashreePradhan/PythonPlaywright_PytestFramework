"""Cart Page Object for Sauce Demo."""

from .base_page import BasePage
from utils.page_helpers import SelectorHelper


class CartPage(BasePage):
    """Page Object Model for the cart page."""

    CHECKOUT_BUTTON = SelectorHelper.checkout_button()

    def __init__(self, page):
        super().__init__(page)

    def click_checkout(self) -> None:
        self.click(self.CHECKOUT_BUTTON)
