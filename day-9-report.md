Day 9 Report – Detection Validation and False Positive Analysis

1. Objective

The objective of Day 9 was to validate the log analyser's detection
rules using normal and suspicious simulated login activities.

2. Normal Login Test

A normal test log file was created with:

- 1 failed login attempt.
- 1 successful login.
- 1 session opened event.

Result: The analyser detected one failed login attempt and one 
successful login. No repeated-failure alert was triggered.

3. Suspicious Login Test

A suspicious test log file was created with:

- 3 failed login attempts.
- Source IP address: 192.168.1.90.
- All three attempts occurred within a short period.

Result: The analyser detected all three failed attempts and
triggered the repeated-failure alert.

4. Detection Rule Validation

The detection threshold was tested using two separate scenarios:

- Normal scenario: 1 failed attempt — no alert.
- Suspicious scenario: 3 failed attempts — alert triggered.

The results matched the expected detection behaviour.

5. False Positive Analysis

The normal test did not trigger a repeated-failure alert. This
indicates that the tested normal login scenario was not incorrectly
classified as repeated suspicious activity.

However, broader testing would be required to confirm the rule's
behaviour in other scenarios.

6. Findings and Limitations

- The detection rule successfully identified the tested repeated
login failures.
- The threshold is based on the total number of failures per source
IP in the test file.
- The current rule does not apply a time-window check.
- These were simulated test logs, not actual attack events.
- Further testing is required to evaluate additional false-positive
and false-negative scenarios.

7. Conclusion

Day 9 successfully validated the log analyser using normal and
suspicious simulated login scenarios. The normal test did not
trigger an alert, while the suspicious test triggered the expected
repeated-failure alert.

Day 9 Status: Completed – Detection Validation and False Positive
Analysis.
