Day 11 Report – IP-Wise Failed Login Analysis

1. Objective

The objective of Day 11 was to perform IP-wise analysis of failed login attempts and identify suspicious login activity based on a predefined threshold within a specific time window.

2. Tasks Performed

1. Reviewed the suspicious test log file "data/day-9-suspicious-test.txt".
2. Created a Python script named "scripts/Day-11-ip-analysis.py".
3. Used regular expressions to extract source IP addresses and timestamps from failed password entries.
4. Grouped failed login attempts by source IP address.
5. Configured a detection threshold of 3 failed attempts within 60 seconds.
6. Executed the Python script and verified the analysis output.
7. Saved three screenshots as evidence in the "evidence" folder.

3. Tools and Technologies Used

- Kali Linux
- Python 3
- Visual Studio Code / Mousepad
- Linux Terminal
- Python libraries: "re", "collections", and "datetime"

4. Analysis Results

The script successfully analyzed the suspicious test log file.

Metric| Result
Total Failed Login Events| 3
Unique Source IPs| 1
Source IP Address| 192.168.1.90
Failed Attempts| 3
Detection Threshold| 3 attempts
Time Window| 60 seconds
Detection Status| SUSPICIOUS
Analysis Status| Completed

5. Key Findings

- Three failed login attempts were identified.
- All three attempts originated from the same source IP address: "192.168.1.90".
- The configured threshold of 3 failed attempts within 60 seconds was reached.
- The script generated a suspicious activity alert.
- The analysis was performed using a controlled test log file.

6. Challenges Faced

- Encountered a Python warning related to timestamp parsing.
- Faced syntax and indentation issues while editing the script.
- Corrected the script and executed it successfully.
- Verified that the final output matched the expected test-log results.

7. Learning Outcomes

- Learned how to extract IP addresses and timestamps using regular expressions.
- Understood how to group failed login attempts by source IP.
- Learned how to use a threshold-based detection method.
- Understood how a time window helps identify repeated failed login activity.
- Improved Python debugging and log-analysis skills.

8. Conclusion

Day 11 successfully implemented IP-wise failed login analysis using Python. The script identified 3 failed login attempts from a single source IP address within the configured 60-second window and generated a suspicious activity alert.

This exercise demonstrates a basic defensive security-monitoring technique for identifying repeated authentication failures. The findings are based on synthetic test data and do not establish that a real attack occurred.

9. Evidence

Three screenshots documenting the Day 11 analysis and final successful output have been saved in the project's "evidence" folder.

Project: Linux Log Analysis and Security Monitoring
Day: 11
Status: Completed
