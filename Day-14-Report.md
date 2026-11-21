Day 14 – Final Security Analysis and Cross-Validation

1. Objective

To validate the results of previous security analysis scripts and confirm consistency between standalone and integrated analysis outputs.

2. Day 11 – IP-Wise Failed Login Validation

- Total failed login events: 3
- Unique source IPs: 1
- Source IP: 192.168.1.90
- Failed attempts: 3
- Status: SUSPICIOUS – Threshold reached
- Detection threshold: 3 or more attempts within 60 seconds

3. Day 12 – Authentication Analysis Validation

- Total log lines: 50
- Sudo matches: 35
- Sudo colon matches: 23
- Root sessions opened: 19
- Root sessions closed: 19
- CRON events: 15
- Failed authentication matches: 0
- Session status: BALANCED

4. Day 13 – Integrated Analysis Validation

The integrated security summary was executed successfully. Its Day 11 and Day 12 findings matched the corresponding standalone analysis evidence.

5. Findings

- Repeated failed login activity was identified in the analysed test evidence.
- Root session counts were balanced.
- No failed authentication matches were found in the analysed authentication dataset.
- Integrated and standalone analysis results were consistent.

6. Limitations

The analysis is based on collected log evidence and test data. It does not establish the presence or absence of a live security incident.

7. Conclusion

Day 14 cross-validation was completed successfully. Previous analysis scripts and their integrated results were verified for consistency.
