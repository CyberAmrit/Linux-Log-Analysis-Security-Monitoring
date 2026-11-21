# Day 6 - Linux Log Analysis Project

## 1. Objective
To improve the Linux Authentication Log Analyzer by adding suspicious login activity detection, timestamp handling, and error handling.

## 2. Tasks Completed
- Reviewed and updated the Python log analyzer.
- Fixed timestamp parsing to avoid DeprecationWarning.
- Added FileNotFoundError exception handling for test log files.
- Analyzed failed login attempts.
- Detected invalid user events.
- Identified successful login events.
- Detected repeated failed login attempts from a source IP.

## 3. Analysis Results

| Metric | Result |
|---|---:|
| Timeline Events | 50 |
| Critical Events | 0 |
| Error Events | 0 |
| Warning Events | 0 |
| Info Events | 50 |
| Failed Login Attempts | 3 |
| Invalid User Events | 1 |
| Successful Logins | 1 |
| Source IP | 192.168.1.50 |
| Failed Attempts from IP | 3 |

## 4. Security Alert
Repeated failed login attempts detected!

The analyzer identified 3 failed login attempts from source IP 192.168.1.50 and generated a suspicious activity alert.

## 5. Error Handling
- FileNotFoundError handling was added.
- Python syntax check completed successfully.
- No Traceback or DeprecationWarning appeared during the final analysis run.

## 6. Evidence Saved
- evidence/day-6-analysis.txt
- Day 6 analysis screenshot saved in the evidence folder.

## 7. Conclusion
Day 6 was completed successfully. The analyzer processed 50 timeline events and detected suspicious authentication activity, including repeated failed login attempts.

Suspicious activity analysis completed.
