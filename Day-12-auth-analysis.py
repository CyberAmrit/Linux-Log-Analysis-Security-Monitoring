from pathlib import Path

LOG_FILE = Path("data/sudo-authentication.txt")

print("=" * 70)
print("DAY 12 - AUTHENTICATION LOG ANALYSIS")
print("=" * 70)

if not LOG_FILE.exists():
    print("ERROR: Authentication log file not found.")
    raise SystemExit(1)

with LOG_FILE.open("r", encoding="utf-8", errors="replace") as file:
    logs = file.readlines()

total_lines = len(logs)

sudo_matches = sum("sudo" in line for line in logs)
sudo_colon_matches = sum("sudo:" in line for line in logs)

root_opened = sum("session opened for user root" in line for line in logs)
root_closed = sum("session closed for user root" in line for line in logs)

cron_events = sum("CRON" in line for line in logs)

failure_patterns = (
    "authentication failure",
    "failed password",
    "invalid user"
)

failed_auth = sum(
    any(pattern in line.lower() for pattern in failure_patterns)
    for line in logs
)

print(f"Total Log Lines: {total_lines}")
print("-" * 70)
print(f"Sudo Matches: {sudo_matches}")
print(f"Sudo Colon Matches: {sudo_colon_matches}")
print(f"Root Sessions Opened: {root_opened}")
print(f"Root Sessions Closed: {root_closed}")
print(f"CRON Events: {cron_events}")
print(f"Failed Authentication Matches: {failed_auth}")
print("-" * 70)

if root_opened == root_closed:
    print("Session Count Status: BALANCED")
else:
    print("Session Count Status: DIFFERENCE FOUND")

if failed_auth == 0:
    print("Authentication Failure Status: NO MATCHES FOUND")
else:
    print("Authentication Failure Status: MATCHES DETECTED")

print("=" * 70)
print("DAY 12 ANALYSIS COMPLETED")
print("=" * 70)
