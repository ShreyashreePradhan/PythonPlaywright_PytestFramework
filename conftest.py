import logging
import os

import pytest
from playwright.sync_api import sync_playwright

from utils.report_paths import LOGS_DIR, SCREENSHOTS_DIR, ensure_artifact_dirs


def pytest_addoption(parser):
    parser.addoption(
        "--pw-browser",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit"],
        help="Browser to run tests against.",
    )
    parser.addoption(
        "--pw-headed",
        action="store_true",
        default=False,
        help="Run tests with a headed browser.",
    )
    parser.addoption(
        "--pw-base-url",
        action="store",
        default=os.getenv("BASE_URL", "https://www.saucedemo.com/"),
        help="Base URL for the application under test.",
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--pw-base-url")


@pytest.fixture(scope="session")
def playwright_instance():
    p = sync_playwright().start()
    yield p
    p.stop()


@pytest.fixture(scope="function")
def browser(playwright_instance, request):
    browser_name = request.config.getoption("--pw-browser")
    headless = not request.config.getoption("--pw-headed")
    browser_launcher = getattr(playwright_instance, browser_name)
    browser = browser_launcher.launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture(scope="function", autouse=True)
def failure_logger(request):
    """Create a per-test log file for failure analysis on every test."""
    ensure_artifact_dirs()
    log_dir = LOGS_DIR

    logger = logging.getLogger(f"pytest.failure.{request.node.name}")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.propagate = False

    log_file = log_dir / f"{request.node.name}.log"
    handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)

    logger.info("Starting test: %s", request.node.nodeid)
    yield logger

    logger.info("Finished test: %s", request.node.nodeid)
    logger.removeHandler(handler)
    handler.close()


@pytest.fixture(scope="function")
def page(browser, base_url):
    context = browser.new_context()
    page = context.new_page()
    page.goto(base_url)
    yield page
    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        logger = item.funcargs.get("failure_logger")
        ensure_artifact_dirs()
        screenshots_dir = SCREENSHOTS_DIR

        if logger:
            logger.error("Test failed: %s", item.nodeid)

        if page:
            screenshot_path = screenshots_dir / f"{item.name}.png"
            try:
                page.screenshot(path=screenshot_path, full_page=True)
            except Exception as exc:
                if logger:
                    logger.error("Screenshot capture failed: %s", exc)
            else:
                if logger:
                    logger.error("Failure screenshot saved to %s", screenshot_path)
