"""Base Page class with common Playwright helpers."""

from playwright.sync_api import Page


class BasePage:
    """Base class for all page objects."""

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str) -> None:
        """Navigate to a URL."""
        self.page.goto(url)

    def is_visible(self, selector: str) -> bool:
        """Check if a selector is visible."""
        return self.page.locator(selector).is_visible()

    def get_text(self, selector: str) -> str:
        """Return text content for a selector."""
        return self.page.locator(selector).text_content()

    def click(self, selector: str) -> None:
        """Click a selector."""
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str) -> None:
        """Fill input text."""
        self.page.locator(selector).fill(text)
