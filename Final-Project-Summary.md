Final Project Summary

Linux Log Analysis and Security Monitoring

1. Project Overview

This project focuses on Linux log analysis and basic security monitoring. It was completed as a 15-day cybersecurity internship project using Kali Linux and Python.

The main purpose was to examine system authentication logs, identify security-related events, detect suspicious login patterns, and prepare structured security reports.

2. Project Objectives

- Understand Linux authentication and system logs.
- Collect and analyze sudo-related events.
- Generate timelines from log entries.
- Classify events using basic severity keywords.
- Identify failed login attempts and invalid users.
- Perform IP-wise failed login analysis.
- Analyze authentication sessions.
- Validate analysis results using test log data.
- Prepare security findings and documentation.

3. Tools and Environment

- Operating System: Kali Linux
- Virtualization: VMware
- Programming Language: Python 3
- Log Collection: journalctl
- Text Editor: Mousepad
- Evidence: Terminal outputs, saved text files and screenshots

4. Methodology

The project was completed through the following stages:

1. Set up the Kali Linux environment and project directory.
2. Collected Linux authentication and system log information.
3. Developed Python scripts for log parsing and timeline generation.
4. Added basic severity classification.
5. Analyzed failed login attempts and invalid-user events using test logs.
6. Examined sudo activity and authentication sessions.
7. Performed IP-wise failed login analysis.
8. Conducted authentication analysis and session-count validation.
9. Generated an integrated security summary.
10. Cross-validated results from previous analysis stages.
11. Saved daily reports, analysis outputs and screenshots as evidence.

5. Key Results and Observations

Baseline log analysis:

- Total analyzed log lines: 50
- Sudo-related matches: 35
- Sudo colon matches: 23
- Root sessions opened: 19
- Root sessions closed: 19
- CRON-related events: 15
- Failed authentication matches: 0
- Session status: Balanced

Controlled suspicious-login test:

- Failed login attempts detected: 3
- Invalid users detected: 1
- Successful login events: 1
- A repeated-failure alert was triggered.

IP-wise analysis:

- Unique source IP identified: 192.168.1.90
- Failed attempts: 3
- Detection status: Suspicious — threshold reached.

6. Challenges Faced

- Understanding Linux authentication log formats.
- Parsing different types of log entries.
- Handling timestamp formats.
- Identifying relevant security events.
- Testing detection logic with sample log data.
- Maintaining consistency between standalone and integrated analysis outputs.

7. Learning Outcomes

- Practical understanding of Linux authentication logs.
- Basic Python scripting for security log analysis.
- Understanding sudo and root session events.
- Identifying repeated failed login patterns.
- Performing source-IP-based analysis.
- Validating results and maintaining evidence.
- Preparing structured cybersecurity reports.

8. Limitations

- The analysis uses collected baseline logs and controlled test datasets.
- Detection logic is primarily keyword- and threshold-based.
- The results do not establish that a real-world security incident occurred.
- This project is a foundational learning implementation, not a production SIEM solution.

9. Conclusion

The 15-day project provided practical experience in Linux log analysis and basic security monitoring. It covered log collection, Python-based analysis, authentication monitoring, suspicious login detection, IP-wise analysis, result validation and technical documentation.

The project strengthened foundational cybersecurity skills and provided an introduction to security monitoring workflows.

10. Future Scope

- Add more advanced log-parsing techniques.
- Integrate additional Linux log sources.
- Improve detection rules and alert generation.
- Explore dashboard-based security monitoring.
- Study integration with professional SIEM platforms.

Project Status

Technical analysis, daily reporting, evidence collection and final documentation completed.
