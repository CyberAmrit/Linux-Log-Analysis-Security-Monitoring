Linux Log Analysis and Security Monitoring

Project Overview

This project focuses on analyzing Linux authentication and system logs to identify security-related events and suspicious login activity.

The project was completed as a 15-day cybersecurity internship project using Kali Linux and Python.

Objectives

- Collect and examine Linux authentication logs.
- Analyze sudo and authentication-related events.
- Identify failed login attempts and invalid users.
- Perform IP-wise failed login analysis.
- Detect repeated failed login patterns using a defined threshold.
- Generate security summaries and daily analysis reports.

Tools and Technologies

- Operating System: Kali Linux
- Virtualization: VMware
- Programming Language: Python 3
- Log Analysis: Linux journalctl and authentication logs
- Editor: Mousepad
- Version Control / Submission: GitHub (planned)

Project Structure

Project-1-Log-Analysis/
├── data/
├── evidence/
├── report/
├── scripts/
└── README.md

- "data/" — Collected logs and test log files.
- "evidence/" — Screenshots and saved analysis outputs.
- "report/" — Daily project reports.
- "scripts/" — Python scripts used for log analysis.

Key Activities

1. Linux environment setup and log collection.
2. Authentication and sudo log analysis.
3. Timeline generation and severity classification.
4. Failed login and invalid-user detection.
5. Suspicious IP analysis.
6. Authentication session analysis.
7. Integrated security summary.
8. Cross-validation of previous analysis results.

Key Findings

The analyzed baseline log dataset contained:

- 50 total log lines.
- 35 sudo-related matches.
- 19 root sessions opened.
- 19 root sessions closed.
- 15 CRON-related events.
- 0 failed authentication matches in the analyzed baseline dataset.

Separate test datasets were also used to validate suspicious login detection. These included repeated failed login attempts and IP-wise analysis.

Important Note

This project uses collected logs and controlled test log entries for learning and validation. The results demonstrate basic log-analysis and detection logic; they do not establish that a real-world security incident occurred.

The detection methods are primarily keyword- and threshold-based and are not a replacement for a production Security Information and Event Management (SIEM) system.

Learning Outcomes

- Understanding Linux authentication logs.
- Using Python for basic security log analysis.
- Identifying suspicious login patterns.
- Analyzing source IP addresses and authentication sessions.
- Generating structured security reports.
- Understanding the importance of evidence and validation.

Conclusion

This project provided practical experience in Linux log analysis and basic security monitoring. It helped develop foundational skills in authentication-event analysis, suspicious activity detection, Python scripting, and security documentation.
