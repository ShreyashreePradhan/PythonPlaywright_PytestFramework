# Simple Playwright + pytest Login Tests

Minimal setup to test login on https://www.saucedemo.com/

## Quick Start

```bash
# 1. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt
playwright install

# 3. Run tests
pytest -v

# 4. Run with headed browser (see browser window)
pytest -v --headed
```

## Folder Structure

```
PWPYTHON_FRAMEWORK/
├── pages/
│   └── login_page.py      # Page Object for login
├── tests/
│   └── test_login.py      # Login tests
├── conftest.py            # Pytest configuration & fixtures
├── pytest.ini             # Pytest settings
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## Test Credentials

Valid credentials for saucedemo:
- Username: `standard_user`
- Password: `secret_sauce`

Other valid usernames: `locked_out_user`, `problem_user`, `performance_glitch_user`

## Run Options

Run all tests:
```bash
pytest -v
```

Run specific test:
```bash
pytest -v tests/test_login.py::test_successful_login
```

Run with headed browser:
```bash
pytest -v --headed
```

Run with browser slowdown (1000ms):
```bash
pytest -v --slowmo=1000
```
