"""Generate per-run pytest reports under reports/run_<n>."""

import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from utils.report_paths import ARTIFACTS_DIR, LOGS_DIR, REPORTS_DIR, SCREENSHOTS_DIR, ensure_artifact_dirs


def next_run_number() -> int:
    """Return the next available run number under reports/."""
    if not REPORTS_DIR.exists():
        return 1

    existing_runs = [path.name for path in REPORTS_DIR.glob("run_*") if path.is_dir()]
    run_numbers = []
    for name in existing_runs:
        try:
            run_numbers.append(int(name.split("_")[1]))
        except (IndexError, ValueError):
            continue

    return max(run_numbers, default=0) + 1


def copy_artifacts(run_dir: Path) -> None:
    logs_target = run_dir / "logs"
    screenshots_target = run_dir / "screenshots"

    ensure_artifact_dirs()
    if LOGS_DIR.exists():
        shutil.copytree(LOGS_DIR, logs_target, dirs_exist_ok=True)

    if SCREENSHOTS_DIR.exists():
        shutil.copytree(SCREENSHOTS_DIR, screenshots_target, dirs_exist_ok=True)


def parse_junit(path: Path) -> dict:
    tree = ET.parse(path)
    root = tree.getroot()

    suites = root.findall(".//testsuite") or [root]
    total = sum(int(s.attrib.get("tests", 0)) for s in suites)
    failures = sum(int(s.attrib.get("failures", 0)) for s in suites)
    errors = sum(int(s.attrib.get("errors", 0)) for s in suites)
    skipped = sum(int(s.attrib.get("skipped", 0)) for s in suites)

    passed = total - failures - errors - skipped
    pass_rate = round((passed / total) * 100, 1) if total else 0.0

    return {
        "total": total,
        "passed": passed,
        "failed": failures + errors,
        "skipped": skipped,
        "pass_rate": pass_rate,
    }


def generate_summary(run_dir: Path, stats: dict, duration_minutes: int) -> None:
    summary = f"""Execution Summary

Total Tests : {stats['total']}
Passed      : {stats['passed']}
Failed      : {stats['failed']}
Pass Rate   : {stats['pass_rate']}%

Build Number: {run_dir.name.split('_')[1]}
Environment : QA
Duration    : {duration_minutes} mins
"""
    (run_dir / "summary.txt").write_text(summary, encoding="utf-8")


def main() -> int:
    ensure_artifact_dirs()
    run_number = next_run_number()
    run_dir = REPORTS_DIR / f"run_{run_number}"
    run_dir.mkdir(exist_ok=True)

    html_path = run_dir / "report.html"
    xml_path = run_dir / "results.xml"

    start = time.time()
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "-v",
        "--html",
        str(html_path),
        "--self-contained-html",
        "--junitxml",
        str(xml_path),
    ]

    result = subprocess.run(cmd, cwd=REPO_ROOT)

    duration_minutes = max(1, int((time.time() - start) // 60))
    copy_artifacts(run_dir)

    if ARTIFACTS_DIR.exists():
        shutil.rmtree(ARTIFACTS_DIR)

    if xml_path.exists():
        stats = parse_junit(xml_path)
        generate_summary(run_dir, stats, duration_minutes)
    else:
        generate_summary(run_dir, {"total": 0, "passed": 0, "failed": 0, "pass_rate": 0.0}, duration_minutes)

    print(f"\nReport generated at: {run_dir}")
    print(f"Summary saved to: {run_dir / 'summary.txt'}")
    print(f"Results XML: {xml_path}")
    print(f"HTML Report: {html_path}")

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
