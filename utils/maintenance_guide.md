# Maintenance Guide

Use this folder when the Sauce Demo UI changes.

## Where to update changes

1. Selectors
   - Update selectors in config/selectors.py.
   - These constants are the single source of truth for page objects.

2. Page objects
   - Update page-specific methods in pages/.
   - Example: login_page.py, inventory_page.py, cart_page.py, checkout_page.py.

3. Test cases
   - Update or extend tests in tests/.
   - Keep business flow assertions here.

## Recommended workflow

- If a button, input, or URL changes: update config/selectors.py first.
- If the user journey changes: update the relevant page object.
- If the expected result changes: update the test case in tests/.

## Failure reporting

- Logs are written to reports/artifacts/logs/<test-name>.log for every test run.
- Screenshots are saved to reports/artifacts/screenshots/<test-name>.png when a test fails.
- The report generator copies these artifacts into reports/run_<n>/ so the final bundle stays in one place.
- Use the demo test tests/test_failure_logging_demo.py to see this behavior in action.
- For CI/local report bundles, run `python utils/generate_reports.py` to create reports/run_<n>/ with logs, report.html, results.xml, screenshots, and summary.txt.

## Quick validation

Run:

```bash
pytest -v
```

This confirms the core login and checkout flows still work after UI updates.
