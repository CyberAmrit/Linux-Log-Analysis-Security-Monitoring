# Project 1: Linux Log Analyzer
# Day 3 - Cybersecurity Internship

from datetime import datetime
log_file = "data/sudo-authentication.txt"

total_lines = 0
sudo_events = 0
session_opened = 0
session_closed = 0
cron_events = 0
auth_failures = 0

events = []
def extract_timestamp(line):
    try:
        timestamp_text = " ".join(line.split()[:3])
        return datetime.strptime(timestamp_text + " 2026","%b %d %H:%M:%S %Y")
    except ValueError:
        return None 

def identify_event(line):
    if "session opened" in line:
        return "SESSION OPENED"
    elif "session closed" in line:
        return "SESSION CLOSED"
    elif "sudo[" in line:
        return "SUDO"
    elif "CRON[" in line:
        return "CRON"
    else:
        return "OTHER"

def build_timeline():
    with open(log_file, "r") as file:
        for line in file:
            timestamp = extract_timestamp(line)

            if timestamp is not None:
                event_type = identify_event(line)

                events.append({
                    "timestamp": timestamp,
                    "event": event_type,
                    "details": line.strip()
                })

def sort_timeline():
    events.sort(key=lambda item: item["timestamp"])

def display_timeline():
    print("\nAUTHENTICATION EVENT TIMELINE")
    print("-" * 60)

    for item in events:
        print(
            item["timestamp"].strftime("%b %d %H:%M:%S"),
            "|",
            item["event"],
            "|",
            item["details"].strip()
        )

print("\nBuilding event timeline...")

build_timeline()
sort_timeline()
display_timeline()

print("\nTotal timeline events:", len(events))

print("=" * 45)
print("LINUX AUTHENTICATION LOG ANALYZER")
print("=" * 45)

try:
    with open(log_file, "r") as file:
        for line in file:
            total_lines += 1

            if "sudo[" in line:
                sudo_events += 1

            if "session opened" in line:
                session_opened += 1

            if "session closed" in line:
                session_closed += 1

            if "CRON[" in line:
                cron_events += 1

            if "authentication failure" in line.lower():
                auth_failures += 1

    print("\nANALYSIS RESULTS")
    print("-" * 45)
    print("Total log lines:", total_lines)
    print("Sudo events:", sudo_events)
    print("Sessions opened:", session_opened)
    print("Sessions closed:", session_closed)
    print("Cron events:", cron_events)
    print("Authentication failure matches:", auth_failures)

    print("\nAnalysis completed successfully.")

except FileNotFoundError:
    print("ERROR: Log file not found.")

print("=" * 45)
print("\nLOG SEVERITY CLASSIFICATION")
print("-" * 45)

severity_counts = {
    "CRITICAL": 0,
    "ERROR": 0,
    "WARNING": 0,
    "INFO": 0
}

with open(log_file, "r") as file:
    for line in file:
        log = line.lower()

        if "critical" in log or "emergency" in log:
            severity = "CRITICAL"

        elif "error" in log:
            severity = "ERROR"

        elif ("warning" in log or
              "authentication failure" in log or
              "failed password" in log):
            severity = "WARNING"

        else:
            severity = "INFO"

        severity_counts[severity] += 1

print("\nSEVERITY SUMMARY")
print("-" * 45)

for severity, count in severity_counts.items():
    print(severity, ":", count)

print("\nSeverity classification completed.")
# ==========================================
# DAY 5 - SUSPICIOUS ACTIVITY DETECTION
# ==========================================

test_log_file = "data/day-9-suspicious-test.txt"

failed_attempts = {}
invalid_user_events = 0
successful_logins = 0

try:
   with open(test_log_file, "r") as file:
    for line in file:
        log = line.lower()

        if "failed password" in log:
            parts = log.split(" from ", 1)

            if len(parts) == 2:
                source_ip = parts[1].split()[0]

                failed_attempts[source_ip] = (
                    failed_attempts.get(source_ip, 0) + 1
                )

        if "invalid user" in log:
            invalid_user_events += 1

        if "accepted password" in log:
            successful_logins += 1

except FileNotFoundError:
  print("ERROR: Test log file not found.")


print("\nSUSPICIOUS ACTIVITY DETECTION")
print("-" * 45)

total_failed = sum(failed_attempts.values())

print("Failed login attempts:", total_failed)
print("Invalid user events:", invalid_user_events)
print("Successful logins:", successful_logins)

print("\nSOURCE IP ANALYSIS")
print("-" * 45)

for ip, count in failed_attempts.items():
    print(ip, ":", count, "failed attempts")

    if count >= 3:
        print("ALERT: Repeated failed login attempts detected!")

print("\nSuspicious activity analysis completed.")
