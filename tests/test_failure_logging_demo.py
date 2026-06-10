"""Demo test that intentionally fails to show logging and screenshot capture."""
import pytest
from pages.login_page import LoginPage

# @pytest.mark.xfail
def test_failure_logging_demo(page, failure_logger):
    """This test is expected to fail so the failure-reporting hooks can be shown.

    It logs the steps in plain English and then intentionally fails.
    """
    failure_logger.info("Step 1: Open the Sauce Demo login page.")
    login_page = LoginPage(page)

    failure_logger.info("Step 2: Try logging in with standard demo credentials.")
    login_page.login("standard_user", "secret_sauce")

    failure_logger.info("Step 3: The next check is intentionally wrong to trigger a failure report.")
    assert "this-intentional-failure" in page.url, "Intentional failure to demonstrate logs and screenshots on error."
