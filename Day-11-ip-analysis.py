import re
from collections import defaultdict
from datetime import datetime

LOG_FILE = "data/day-9-suspicious-test.txt"
THRESHOLD_ATTEMPTS = 3
TIME_WINDOW_SECONDS = 60

failed_attempts = defaultdict(list)

# Read and analyse log entries
with open(LOG_FILE, "r") as file:
    for line in file:
        if "Failed password" not in line:
            continue

        ip_match = re.search(
            r"from (\d{1,3}(?:\.\d{1,3}){3})", line
        )

        time_match = re.match(
            r"([A-Z][a-z]{2}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})",
            line
        )

        if ip_match and time_match:
            ip = ip_match.group(1)

            timestamp = datetime.strptime(
                f"{datetime.now().year} {time_match.group(1)}",
                "%Y %b %d %H:%M:%S"
            )

            failed_attempts[ip].append(timestamp)

# Display analysis results
print("=" * 50)
print("DAY 11 - IP-WISE FAILED LOGIN ANALYSIS")
print("=" * 50)

total_events = sum(len(times) for times in failed_attempts.values())

print(f"Total Failed Login Events: {total_events}")
print(f"Unique Source IPs: {len(failed_attempts)}")
print("-" * 50)

if not failed_attempts:
    print("No failed login events found.")

for ip, times in sorted(failed_attempts.items()):
    times.sort()
    count = len(times)

    suspicious = any(
        (times[i + THRESHOLD_ATTEMPTS - 1] - times[i]).total_seconds()
        <= TIME_WINDOW_SECONDS
        for i in range(len(times) - THRESHOLD_ATTEMPTS + 1)
    )

    print(f"Source IP: {ip}")
    print(f"Failed Attempts: {count}")

    if suspicious:
        print("Status: SUSPICIOUS - Threshold reached")
        print("Reason: 3 or more attempts within 60 seconds")
    else:
        print("Status: NO ALERT - Threshold not reached")

    print("-" * 50)

print("Analysis completed.")
