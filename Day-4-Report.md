Day 4 – Log Severity Classification

Project

Linux Log Analysis – Cybersecurity Internship

Objective

To extend the Linux Log Analyzer by adding keyword-based log severity classification.

Work Performed

1. Reviewed the authentication log file.
2. Created a backup of the Day 3 Python script.
3. Added severity classification logic to the analyzer.
4. Classified log entries into four categories:
   - CRITICAL
   - ERROR
   - WARNING
   - INFO
5. Executed the updated Python script successfully.
6. Saved the analysis output in "evidence/day-4-analysis.txt".
7. Captured screenshots of the execution output.

Analysis Results

Metric| Result
Total log lines| 50
Sudo events| 35
Sessions opened| 19
Sessions closed| 19
Cron events| 15
Authentication failure matches| 0
CRITICAL| 0
ERROR| 0
WARNING| 0
INFO| 50

Observation

All 50 log entries were classified as INFO because none matched the configured CRITICAL, ERROR, or WARNING keywords.

Note: This is a basic keyword-based classification, not an official system log severity assessment.

Conclusion

The Day 4 enhancement was implemented and tested successfully. The analyzer now displays a severity summary along with the existing authentication event analysis.

Evidence

- "evidence/day-4-analysis.txt"
- Day 4 execution screenshots
