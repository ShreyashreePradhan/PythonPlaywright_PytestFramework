"""Simple Login Tests"""

from config.test_data import INVALID_USER, VALID_USER
from pages.login_page import LoginPage


def test_successful_login(page):
    """Test successful login with valid credentials"""
    login_page = LoginPage(page)
    login_page.login(VALID_USER["username"], VALID_USER["password"])
    
    # Check if we're on inventory page (URL changes)
    assert "inventory" in page.url


def test_invalid_credentials(page):
    """Test login with invalid credentials"""
    login_page = LoginPage(page)
    login_page.login(INVALID_USER["username"], INVALID_USER["password"])
    
    # Check if error is displayed
    assert login_page.is_error_displayed()
    error = login_page.get_error_text()
    assert "not match" in error.lower()


def test_empty_username(page):
    """Test login with empty username"""
    login_page = LoginPage(page)
    login_page.login("", VALID_USER["password"])
    
    # Check if error is displayed
    assert login_page.is_error_displayed()


def test_empty_password(page):
    """Test login with empty password"""
    login_page = LoginPage(page)
    login_page.login(VALID_USER["username"], "")
    
    # Check if error is displayed
    assert login_page.is_error_displayed()
