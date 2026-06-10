"""Login Page Object for Sauce Demo."""

from .base_page import BasePage
from utils.page_helpers import SelectorHelper


class LoginPage(BasePage):
    """Page Object Model for the login page."""

    USERNAME_INPUT = SelectorHelper.login_username()
    PASSWORD_INPUT = SelectorHelper.login_password()
    LOGIN_BUTTON = SelectorHelper.login_button()
    ERROR_MESSAGE = SelectorHelper.login_error()

    def __init__(self, page):
        super().__init__(page)

    def enter_username(self, username: str) -> None:
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> None:
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)

    def get_error_text(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
