# Sauce Demo Playwright + pytest Framework

This framework automates the Sauce Demo purchase flow using Playwright, pytest, and Page Object Model (POM). It is designed to be easy to extend for new testers and to keep selectors, data, and reports in one place.

## What this project covers

- Login page validation
- Inventory and cart flow
- Checkout flow until order completion
- Failure logging and screenshots on failed tests
- Per-run report generation under reports/run_<n>

## Quick Start

```bash
# 1. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt
playwright install

# 3. Run the main test suite
pytest -v

# 4. Run with a visible browser window
pytest -v --pw-headed

# 5. Generate a fresh report bundle
python utils/generate_reports.py
```

## Folder Structure

```text
PWPYTHON_FRAMEWORK/
├── config/                # Central selectors and test data
│   ├── selectors.py
│   └── test_data.py
├── pages/                 # Page Object Model classes
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── tests/                 # Test cases
│   ├── test_checkout_flow.py
│   ├── test_failure_logging_demo.py
│   └── test_login.py
├── utils/                 # Reusable helpers and report generation
│   ├── generate_reports.py
│   ├── maintenance_guide.md
│   ├── page_helpers.py
│   └── report_paths.py
├── conftest.py            # Pytest fixtures, CLI options, failure hooks
├── pytest.ini             # Pytest settings
├── requirements.txt       # Python dependencies
└── reports/               # Generated report folders: run_1, run_2, ...
```

## How the flow works

1. The browser opens from `conftest.py` using Playwright.
2. The page object classes in `pages/` perform the actions for each screen.
3. Tests in `tests/` use centralized data from `config/test_data.py`.
4. When a test fails, screenshots and logs are stored under `reports/artifacts/` and then packaged into `reports/run_<n>/` by `utils/generate_reports.py`.

## Adding your own test case

1. Create a new test in `tests/` using pytest naming rules, for example `tests/test_my_flow.py`.
2. Reuse existing page objects in `pages/` instead of writing selectors directly in the test.
3. Add any new selectors to `config/selectors.py`.
4. Add test data to `config/test_data.py` when the scenario needs usernames, passwords, or checkout details.
5. Run the test with:

```bash
pytest -v tests/test_my_flow.py
```

6. Generate the report bundle with:

```bash
python utils/generate_reports.py
```

## Useful commands

Run all tests:
```bash
pytest -v
```

Run one test:
```bash
pytest -v tests/test_login.py::test_successful_login
```

Run in headed mode:
```bash
pytest -v --pw-headed
```

Run on a specific browser:
```bash
pytest -v --pw-browser=firefox
```

Generate reports:
```bash
python utils/generate_reports.py
```

## Report folders

- `reports/run_1/` contains the first generated report bundle
- `reports/run_2/` is created automatically on the next run
- Each run folder includes `report.html`, `results.xml`, `logs/`, `screenshots/`, and `summary.txt`
