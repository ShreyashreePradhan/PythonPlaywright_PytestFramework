"""Central selector configuration for Sauce Demo UI tests.

Update selectors here whenever the website changes.
"""

LOGIN = {
    "username": "#user-name",
    "password": "#password",
    "login_button": "#login-button",
    "error_message": "[data-test='error']",
}

INVENTORY = {
    "inventory_list": ".inventory_list",
    "add_to_cart_buttons": "button[id^='add-to-cart']",
    "cart_link": ".shopping_cart_link",
    "cart_badge": ".shopping_cart_badge",
}

CHECKOUT = {
    "checkout_button": "button[data-test='checkout']",
    "continue_button": "#continue",
    "finish_button": "#finish",
    "first_name": "input[data-test='firstName']",
    "last_name": "input[data-test='lastName']",
    "postal_code": "input[data-test='postalCode']",
    "complete_header": ".complete-header",
}

URLS = {
    "base": "https://www.saucedemo.com/",
    "inventory": "https://www.saucedemo.com/inventory.html",
    "checkout_step_one": "https://www.saucedemo.com/checkout-step-one.html",
    "checkout_complete": "https://www.saucedemo.com/checkout-complete.html",
}
