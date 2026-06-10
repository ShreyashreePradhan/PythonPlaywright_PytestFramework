"""Checkout Page Object for Sauce Demo."""

from .base_page import BasePage
from utils.page_helpers import SelectorHelper


class CheckoutPage(BasePage):
    """Page Object Model for the checkout flow."""

    FIRST_NAME_INPUT = SelectorHelper.first_name_input()
    LAST_NAME_INPUT = SelectorHelper.last_name_input()
    POSTAL_CODE_INPUT = SelectorHelper.postal_code_input()
    CONTINUE_BUTTON = SelectorHelper.continue_button()
    FINISH_BUTTON = SelectorHelper.finish_button()
    COMPLETE_HEADER = SelectorHelper.complete_header()

    def __init__(self, page):
        super().__init__(page)

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self) -> None:
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self) -> None:
        self.click(self.FINISH_BUTTON)

    def is_order_complete(self) -> bool:
        return self.is_visible(self.COMPLETE_HEADER) and "thank you for your order" in self.get_text(self.COMPLETE_HEADER).lower()
