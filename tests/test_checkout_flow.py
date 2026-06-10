"""End-to-end checkout flow test for Sauce Demo."""

from config.test_data import CHECKOUT_CUSTOMER, VALID_USER
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_to_checkout_flow(page):
    """Verify a user can log in, add an item, and complete checkout."""
    login_page = LoginPage(page)
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    inventory_page = InventoryPage(page)
    assert inventory_page.is_inventory_visible()

    inventory_page.add_first_product_to_cart()
    assert inventory_page.get_cart_count() == "1"

    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(page)
    checkout_page.fill_customer_info(
        CHECKOUT_CUSTOMER["first_name"],
        CHECKOUT_CUSTOMER["last_name"],
        CHECKOUT_CUSTOMER["postal_code"],
    )
    checkout_page.click_continue()
    checkout_page.click_finish()

    assert "checkout-complete" in page.url
    assert checkout_page.is_order_complete()
