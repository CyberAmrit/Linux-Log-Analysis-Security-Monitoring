Day 8 Report – Security Event Correlation & Comparative Analysis

Project: Linux Log Analysis & Security Monitoring
Day: 8
Date: 15 November 2026

1. Objective

The objective of Day 8 was to correlate authentication log events, simulated suspicious login activity, and sudo command activity to distinguish normal system activity from suspicious authentication patterns.

2. Activities Performed

1. Reviewed the main Linux authentication log.
2. Checked the simulated test log for failed login attempts, invalid users, and successful logins.
3. Reviewed Day 7 sudo command verification results.
4. Compared the findings from the separate datasets.
5. Documented the correlation observations.

3. Results and Observations

A. Main Authentication Log

- Total log lines: 50
- Failed password matches: 0
- Invalid user matches: 0
- Accepted password matches: 0

B. Simulated Test Log

- Failed password attempts: 3
- Invalid user events: 1
- Successful login events: 1
- Repeated failed attempts source IP: "192.168.1.50"
- Invalid user source IP: "192.168.1.60"
- Successful login source IP: "192.168.1.70"

C. Sudo Command Review

- Total verified command entries: 12
- journalctl commands: 8
- systemctl commands: 4
- No matching events found for the checked suspicious patterns.

4. Correlation Analysis

The main authentication log and simulated test log were analyzed separately.

The main authentication log contained no matches for the three checked authentication patterns. In contrast, the simulated test log contained three failed password attempts from "192.168.1.50", followed by an invalid-user event from another IP and a successful login from a third IP.

The sudo command review showed activity related to system log inspection and SSH service status checks.

The repeated failed-login alert was detected in the simulated test dataset.

5. Conclusion

Day 8 successfully demonstrated how authentication events and privilege-related activity can be compared across separate datasets. The analysis identified repeated failed login attempts in the simulated test data and distinguished them from the main system log activity.

6. Learning Outcomes

- Learned the importance of correlating security events.
- Understood the difference between actual system logs and simulated test logs.
- Practiced identifying repeated authentication failures.
- Reviewed sudo command activity.
- Improved security analysis and documentation skills.

7. Evidence

Supporting evidence is saved in:

"evidence/day-8-correlation-analysis.txt"

8. Next Steps

Continue with security findings analysis, severity assessment, and mapping relevant observations to security frameworks where applicable.
