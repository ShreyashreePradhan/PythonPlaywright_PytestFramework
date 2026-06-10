"""Small helper utilities for page objects to read from centralized config."""

from config.selectors import CHECKOUT, INVENTORY, LOGIN


class SelectorHelper:
    """Read centralized selectors for the current page object."""

    @staticmethod
    def login_username():
        return LOGIN["username"]

    @staticmethod
    def login_password():
        return LOGIN["password"]

    @staticmethod
    def login_button():
        return LOGIN["login_button"]

    @staticmethod
    def login_error():
        return LOGIN["error_message"]

    @staticmethod
    def inventory_list():
        return INVENTORY["inventory_list"]

    @staticmethod
    def add_to_cart_button():
        return INVENTORY["add_to_cart_buttons"]

    @staticmethod
    def cart_link():
        return INVENTORY["cart_link"]

    @staticmethod
    def cart_badge():
        return INVENTORY["cart_badge"]

    @staticmethod
    def checkout_button():
        return CHECKOUT["checkout_button"]

    @staticmethod
    def continue_button():
        return CHECKOUT["continue_button"]

    @staticmethod
    def finish_button():
        return CHECKOUT["finish_button"]

    @staticmethod
    def first_name_input():
        return CHECKOUT["first_name"]

    @staticmethod
    def last_name_input():
        return CHECKOUT["last_name"]

    @staticmethod
    def postal_code_input():
        return CHECKOUT["postal_code"]

    @staticmethod
    def complete_header():
        return CHECKOUT["complete_header"]
