from pathlib import Path
from datetime import datetime

PROJECT_DIR = Path(__file__).resolve().parent.parent
DAY11_FILE = PROJECT_DIR / "evidence" / "day-11-ip-analysis.txt"
DAY12_FILE = PROJECT_DIR / "evidence" / "day-12-auth-analysis.txt"
OUTPUT_FILE = PROJECT_DIR / "evidence" / "day-13-security-summary.txt"

print("=" * 55)
print("DAY 13 - INTEGRATED SECURITY MONITORING SUMMARY")
print("=" * 55)

print("Analysis Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

for title, file_path in [
    ("DAY 11 - IP-WISE FAILED LOGIN ANALYSIS", DAY11_FILE),
    ("DAY 12 - AUTHENTICATION LOG ANALYSIS", DAY12_FILE),
]:
    print(f"\n{title}")
    print("-" * 55)

    if file_path.exists():
        content = file_path.read_text(errors="replace").strip()
        print(content if content else "Evidence file is empty.")
    else:
        print(f"Evidence file not found: {file_path.name}")

print("\n" + "=" * 55)
print("SUMMARY: Previous analysis evidence reviewed.")
print("Note: This report consolidates existing findings;")
print("it does not independently verify a live security incident.")
print("=" * 55)
