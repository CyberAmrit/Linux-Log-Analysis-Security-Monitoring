Day 12 – Authentication Log Analysis

1. Objective

The objective of Day 12 was to perform authentication log analysis on Kali Linux and examine sudo activity, root session events, CRON activity, and failed authentication patterns.

2. Environment

- Operating System: Kali Linux
- Platform: VMware
- Programming Language: Python 3
- Log File: "data/sudo-authentication.txt"
- Analysis Script: "scripts/Day-12-auth-analysis.py"

3. Methodology

The following activities were performed:

1. Inspected the original authentication log.
2. Counted general sudo matches and specific sudo colon matches.
3. Analysed root session opening events.
4. Analysed root session closing events.
5. Counted CRON-related events.
6. Checked for authentication failure patterns.
7. Developed and executed a Python script to automate the analysis.

4. Commands Used

head -20 data/sudo-authentication.txt

grep -c 'sudo' data/sudo-authentication.txt

grep -c 'sudo:' data/sudo-authentication.txt

grep -c "session opened for user root" data/sudo-authentication.txt

grep -c "session closed for user root" data/sudo-authentication.txt

grep -c "CRON" data/sudo-authentication.txt

grep -ciE "authentication failure|failed password|invalid user" data/sudo-authentication.txt

python3 scripts/Day-12-auth-analysis.py

5. Analysis Results

Parameter| Result
Total Log Lines| 50
General Sudo Matches| 35
Specific Sudo Colon Matches| 23
Root Sessions Opened| 19
Root Sessions Closed| 19
CRON Events| 15
Failed Authentication Matches| 0

6. Findings

- The authentication log contained 50 lines.
- General sudo keyword matching returned 35 results.
- Specific "sudo:" matching returned 23 results.
- Root session opening and closing counts were both 19.
- A total of 15 CRON-related log lines were identified.
- No matches were found for the selected failed authentication patterns.
- Root session counts were balanced at the aggregate level.

7. Python Automation

A Python script named "Day-12-auth-analysis.py" was created.

The script automatically:

- Reads the authentication log file.
- Counts sudo-related patterns.
- Counts root session opening and closing events.
- Counts CRON events.
- Searches for selected authentication failure patterns.
- Displays an authentication analysis summary.

The script executed successfully without errors.

8. Limitations

- The analysis was performed on the available 50-line authentication log file only.
- Keyword-based matching may not identify every possible authentication event.
- Equal session opening and closing counts do not independently prove that every session was correctly paired.
- Zero matching failure patterns do not establish that the entire system had no failed login attempts.

9. Conclusion

Day 12 successfully completed the authentication log analysis task.

The analysis identified sudo activity, root session events, CRON activity, and selected authentication failure patterns.

Python automation was successfully implemented to generate a repeatable authentication summary.

This exercise improved practical understanding of Linux authentication logs and basic security monitoring techniques.
