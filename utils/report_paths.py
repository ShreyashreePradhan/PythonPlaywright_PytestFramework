"""Centralized report artifact paths for logs and screenshots."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "reports"
ARTIFACTS_DIR = REPORTS_DIR / "artifacts"
LOGS_DIR = ARTIFACTS_DIR / "logs"
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"


def ensure_artifact_dirs() -> None:
    """Create the shared artifact directories used by tests and reports."""
    REPORTS_DIR.mkdir(exist_ok=True)
    ARTIFACTS_DIR.mkdir(exist_ok=True)
    LOGS_DIR.mkdir(exist_ok=True)
    SCREENSHOTS_DIR.mkdir(exist_ok=True)
