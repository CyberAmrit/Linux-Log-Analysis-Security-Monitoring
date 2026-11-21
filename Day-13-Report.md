Day 13 Report – Integrated Security Monitoring Summary

1. Objective

The objective of Day 13 was to consolidate the security analysis findings from Day 11 (IP-wise Failed Login Analysis) and Day 12 (Authentication Log Analysis) into a single security monitoring summary.

2. Environment

- Operating System: Kali Linux
- Programming Language: Python 3
- Project: Linux Log Analysis and Security Monitoring
- Tools: Python, Terminal, Mousepad

3. Methodology

The existing Day 11 and Day 12 analysis evidence files were used as input sources.

A Python script named "Day-13-security-summary.py" was created to:

- Read Day 11 IP-wise failed login analysis evidence.
- Read Day 12 authentication log analysis evidence.
- Display both analysis results in one consolidated summary.
- Report missing evidence files when applicable.

4. Day 11 – IP-Wise Failed Login Findings

- Total Failed Login Events: 3
- Unique Source IPs: 1
- Source IP: 192.168.1.90
- Failed Attempts: 3
- Status: SUSPICIOUS – Threshold reached
- Detection Reason: 3 or more attempts within 60 seconds.

5. Day 12 – Authentication Log Findings

- Total Log Lines: 50
- Sudo Matches: 35
- Sudo Colon Matches: 23
- Root Sessions Opened: 19
- Root Sessions Closed: 19
- CRON Events: 15
- Failed Authentication Matches: 0
- Session Count Status: BALANCED
- Authentication Failure Status: NO MATCHES FOUND

6. Python Automation

The script "scripts/Day-13-security-summary.py" was developed to consolidate the previously generated analysis evidence.

The script successfully displayed the Day 11 and Day 12 findings in one output.

7. Evidence Collected

- "scripts/Day-13-security-summary.py"
- "evidence/day-11-ip-analysis.txt"
- "evidence/day-12-auth-analysis.txt"
- "evidence/day-13-security-summary.txt"
- Day 13 terminal screenshots.

8. Limitations

This activity consolidates previously generated analysis results. It does not perform live monitoring, independently verify an active security incident, or establish that the suspicious login attempts were successful.

9. Conclusion

Day 13 successfully consolidated the IP-wise failed login findings and authentication log analysis into one security monitoring summary.

The previous analysis identified three failed login attempts from one source IP address, while the authentication log analysis showed balanced root sessions and no matching authentication failure patterns.

This activity demonstrates how separate security analysis results can be organized into a consolidated monitoring report.

Day 13 Status: Completed
