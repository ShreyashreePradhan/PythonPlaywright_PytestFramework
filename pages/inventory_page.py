"""Inventory Page Object for Sauce Demo."""

from .base_page import BasePage
from utils.page_helpers import SelectorHelper


class InventoryPage(BasePage):
    """Page Object Model for the inventory page."""

    INVENTORY_LIST = SelectorHelper.inventory_list()
    ADD_TO_CART_BUTTONS = SelectorHelper.add_to_cart_button()
    CART_LINK = SelectorHelper.cart_link()
    CART_BADGE = SelectorHelper.cart_badge()

    def __init__(self, page):
        super().__init__(page)

    def is_inventory_visible(self) -> bool:
        return self.is_visible(self.INVENTORY_LIST)

    def add_first_product_to_cart(self) -> None:
        self.page.locator(self.ADD_TO_CART_BUTTONS).first.click()

    def go_to_cart(self) -> None:
        self.click(self.CART_LINK)

    def get_cart_count(self) -> str:
        return self.get_text(self.CART_BADGE)
