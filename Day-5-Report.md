Day 5 – Suspicious Activity Detection

Objective

To enhance the Linux Log Analyzer by detecting suspicious authentication activities from log data.

Tasks Performed

1. Created a simulated SSH test log file.
2. Detected failed login attempts.
3. Identified invalid user events.
4. Counted successful login events.
5. Grouped failed login attempts by source IP address.
6. Implemented an alert for repeated failed login attempts.
7. Executed and tested the updated Python analyzer.

Test Results

Event| Result
Failed login attempts| 3
Invalid user events| 1
Successful logins| 1
Source IP| 192.168.1.50
Repeated failure alert| Triggered

Alert Generated

"ALERT: Repeated failed login attempts detected!"

The analyzer detected three failed login attempts from the same source IP address (192.168.1.50) and generated an alert based on the project's configured threshold of 3 attempts.

Execution Status

The Python script executed successfully without any fatal errors.

The original authentication log analysis and severity classification continued to work successfully.

Evidence

- "evidence/day-5-analysis.txt"
- Day 5 execution screenshots

Conclusion

Day 5 successfully implemented and tested suspicious authentication activity detection using Python. The analyzer can identify repeated failed login attempts, invalid user events, successful logins, and suspicious source IP activity.

Note: The test log contains simulated entries created for educational testing. The alert threshold of 3 is a project-defined value, not a universal security standard.
